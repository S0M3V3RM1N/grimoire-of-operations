#!/usr/bin/env python3
"""
SSH Default Credential Sweeper
- Tests a small set of common default creds against a list of hosts over SSH.
- Designed for blue-team auditing in controlled environments.

Usage:
  python3 ssh_default_sweeper.py -i targets.txt -o findings.csv
  python3 ssh_default_sweeper.py -i targets.txt -c creds.csv --delay 1.5 --per-host-limit 8

Targets file format:
  One host per line. Optional port and label:
    10.10.10.10
    ap01.local:2222,ap
    printer01.example.com,printer

Creds file format (CSV):
  username,password,label(optional)
    admin,admin,common
    root,root,common
"""

import argparse
import csv
import socket
import sys
import time
from dataclasses import dataclass
from typing import List, Optional, Tuple

try:
    import paramiko
except ImportError:
    print("[!] This script requires 'paramiko'. Install with: pip install paramiko", file=sys.stderr)
    sys.exit(1)

@dataclass
class Target:
    host: str
    port: int
    label: str

@dataclass
class AttemptResult:
    host: str
    port: int
    label: str
    username: str
    password: str
    success: bool
    banner: str
    whoami: str
    error: str

# Small, conservative built-in set you can extend via --creds
BUILTIN_CREDS = [
    ("admin", "admin", "common"),
    ("admin", "password", "common"),
    ("admin", "1234", "printer"),
    ("root", "root", "common"),
    ("root", "toor", "common"),
    ("ubnt", "ubnt", "ap"),
    ("cisco", "cisco", "network"),
    ("vyatta", "vyatta", "network"),
]

def parse_targets(path: str) -> List[Target]:
    targets: List[Target] = []
    with open(path, "r") as f:
        for line in f:
            raw = line.strip()
            if not raw or raw.startswith("#"):
                continue
            label = ""
            hostport = raw
            if "," in raw:
                hostport, label = [x.strip() for x in raw.split(",", 1)]
            host, port = hostport, 22
            if ":" in hostport:
                host, p = hostport.rsplit(":", 1)
                try:
                    port = int(p)
                except ValueError:
                    pass
            targets.append(Target(host=host, port=port, label=label))
    return targets

def load_creds(creds_csv: Optional[str]) -> List[Tuple[str, str, str]]:
    if not creds_csv:
        return BUILTIN_CREDS
    creds: List[Tuple[str, str, str]] = []
    with open(creds_csv, "r", newline="") as f:
        rdr = csv.reader(f)
        for row in rdr:
            if not row or row[0].startswith("#"):
                continue
            if len(row) == 1:
                continue
            username = row[0].strip()
            password = row[1].strip() if len(row) > 1 else ""
            label = row[2].strip() if len(row) > 2 else "custom"
            if username:
                creds.append((username, password, label))
    return creds or BUILTIN_CREDS

def safe_ssh_try(host: str, port: int, username: str, password: str, timeout: float) -> Tuple[bool, str, str, str]:
    """
    Returns: (success, banner, whoami, error)
    - banner: server_id string if handshake succeeds
    - whoami: output of a benign command if shell is available
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    banner, whoami = "", ""
    try:
        # Paramiko emits banner as 'client._transport.remote_version'
        client.connect(
            hostname=host,
            port=port,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False,
            auth_timeout=timeout,
            timeout=timeout,
            banner_timeout=timeout,
        )
        if client.get_transport():
            banner = client.get_transport().remote_version or ""
        # Try a harmless command; some network devices won’t support this gracefully—ignore failures
        try:
            stdin, stdout, stderr = client.exec_command("whoami", timeout=timeout)
            whoami = (stdout.read() or b"").decode(errors="ignore").strip()
        except Exception:
            whoami = ""
        return True, banner, whoami, ""
    except (paramiko.AuthenticationException, paramiko.SSHException) as e:
        return False, banner, whoami, f"ssh_error:{e.__class__.__name__}"
    except (socket.timeout, ConnectionRefusedError, OSError) as e:
        return False, banner, whoami, f"net_error:{e.__class__.__name__}"
    except Exception as e:
        return False, banner, whoami, f"unexpected:{e.__class__.__name__}"
    finally:
        try:
            client.close()
        except Exception:
            pass

def should_try_cred(target: Target, cred_label: str) -> bool:
    """
    Simple heuristic: if target has a label (e.g., 'ap', 'printer'), prefer creds with same label or 'common'.
    If no label, allow all.
    """
    if not target.label:
        return True
    return cred_label.lower() in {target.label.lower(), "common"}

def main():
    ap = argparse.ArgumentParser(description="Audit endpoints for SSH default credentials (blue-team use).")
    ap.add_argument("-i", "--input", required=True, help="Targets file (one host per line; optional ',label' and ':port').")
    ap.add_argument("-o", "--output", default="ssh_default_findings.csv", help="Output CSV path.")
    ap.add_argument("-c", "--creds", default=None, help="CSV of username,password[,label]. If omitted, uses built-ins.")
    ap.add_argument("--timeout", type=float, default=4.0, help="SSH connect/auth timeout (seconds).")
    ap.add_argument("--delay", type=float, default=0.8, help="Delay between attempts (seconds).")
    ap.add_argument("--per-host-limit", type=int, default=10, help="Max credential attempts per host (safety guard).")
    ap.add_argument("--stop-on-success", action="store_true", help="Stop trying more creds for a host after first success.")
    args = ap.parse_args()

    targets = parse_targets(args.input)
    creds = load_creds(args.creds)

    print(f"[+] Loaded {len(targets)} targets; {len(creds)} credential pairs.")
    results: List[AttemptResult] = []

    for t in targets:
        attempts = 0
        host_had_success = False
        for (u, p, lbl) in creds:
            if attempts >= args.per_host_limit:
                break
            if not should_try_cred(t, lbl):
                continue
            attempts += 1
            success, banner, whoami, err = safe_ssh_try(t.host, t.port, u, p, args.timeout)
            results.append(AttemptResult(
                host=t.host,
                port=t.port,
                label=t.label,
                username=u,
                password=p,
                success=success,
                banner=banner,
                whoami=whoami,
                error=err if not success else "",
            ))
            # Console feedback (minimal)
            status = "OK" if success else "FAIL"
            print(f"{t.host}:{t.port} [{t.label or '-'}] {u}:{p} -> {status}")
            if success:
                host_had_success = True
                if args.stop_on_success:
                    break
            time.sleep(args.delay)
        if not host_had_success and attempts == 0:
            # No creds were tried due to label filtering
            results.append(AttemptResult(
                host=t.host, port=t.port, label=t.label,
                username="", password="", success=False,
                banner="", whoami="", error="skipped:no_matching_creds"
            ))

    # Write CSV
    fields = ["host", "port", "label", "username", "password", "success", "banner", "whoami", "error"]
    with open(args.output, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in results:
            w.writerow({
                "host": r.host,
                "port": r.port,
                "label": r.label,
                "username": r.username,
                "password": r.password,
                "success": r.success,
                "banner": r.banner,
                "whoami": r.whoami,
                "error": r.error,
            })

    total = len({(t.host, t.port) for t in targets})
    hits = len({(r.host, r.port) for r in results if r.success})
    print(f"[+] Completed. {hits}/{total} hosts had at least one successful default credential.")

if __name__ == "__main__":
    main()
