#!/usr/bin/env python3
import argparse
import csv
import socket
from ftplib import FTP, error_perm
from datetime import datetime

def check_ftp_anonymous(host: str, timeout: float = 5.0):
    result = {
        "host": host,
        "reachable": False,
        "anonymous_allowed": False,
        "welcome": "",
        "error": ""
    }
    try:
        with FTP() as ftp:
            ftp.connect(host=host, port=21, timeout=timeout)
            result["reachable"] = True
            # Try anonymous login
            welcome = ftp.getwelcome() or ""
            result["welcome"] = welcome.strip()
            ftp.login(user="anonymous", passwd="anonymous@")
            result["anonymous_allowed"] = True
            # If we want to be extra gentle, immediately quit after login
            ftp.quit()
    except (socket.timeout, ConnectionRefusedError) as e:
        result["error"] = f"connect_failed: {type(e).__name__}"
    except OSError as e:
        # Covers DNS errors, network unreachable, etc.
        result["error"] = f"oserror: {e.__class__.__name__}"
    except error_perm as e:
        # 530 Login incorrect, or permission denied
        result["error"] = f"perm_error: {str(e).splitlines()[0]}"
    except Exception as e:
        result["error"] = f"unexpected: {e.__class__.__name__}: {e}"
    return result

def main():
    parser = argparse.ArgumentParser(
        description="Check a list of hosts for anonymous FTP access."
    )
    parser.add_argument("-i", "--input", required=True,
                        help="Path to file containing hosts/IPs (one per line)")
    parser.add_argument("-o", "--output", default=f"ftp_anon_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        help="Output CSV path (default: timestamped)")
    parser.add_argument("-t", "--timeout", type=float, default=5.0,
                        help="Connection timeout in seconds (default: 5)")
    args = parser.parse_args()

    with open(args.input, "r") as f:
        hosts = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]

    results = []
    for host in hosts:
        res = check_ftp_anonymous(host, timeout=args.timeout)
        results.append(res)

    fieldnames = ["host", "reachable", "anonymous_allowed", "welcome", "error"]
    with open(args.output, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    # Quick console summary
    total = len(results)
    anon_ok = sum(1 for r in results if r["anonymous_allowed"])
    print(f"[+] Scanned {total} hosts. Anonymous FTP enabled on {anon_ok}.")
    print(f"[+] Results written to: {args.output}")

if __name__ == "__main__":
    main()
