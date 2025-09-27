# Simple Python Packet Sniffer

A compact, educational packet sniffer written in Python for Linux (AF_PACKET). This project demonstrates raw sockets, Ethernet/IPv4/TCP/UDP parsing, basic anomaly heuristics (SYN-scan and high-rate DNS detection), and optional PCAP output for offline analysis.

> **Warning / Legal:** Run this only on networks and systems you own or where you have explicit authorization to capture traffic. Sniffing other people's traffic is illegal and unethical.

---

## What's included

* `sniffer.py` — single-file Python sniffer that:

  * Opens a raw AF_PACKET socket on a specified interface.
  * Parses Ethernet → IPv4 → TCP/UDP headers.
  * Prints human-readable packet summaries with timestamps.
  * Detects simple suspicious patterns (SYN flood/scan and high-rate DNS queries).
  * Optionally writes raw captures to a PCAP file compatible with Wireshark.

---

## Goals (why this is portfolio-worthy)

* Shows low-level networking knowledge (Ethernet/IP/TCP/UDP) without relying on heavy libraries.
* Demonstrates ability to parse binary protocols, think about endianness, and implement sliding-window heuristics.
* Produces PCAPs that can be used with Wireshark for reproducible analysis and evidence in reports.

---

## Requirements

* Linux (tested on modern Ubuntu/Debian kernels).
* Python 3.8+ (works on 3.10/3.11).
* Root privileges to open raw sockets: `sudo` is required.
* Optional: Wireshark or tcpdump to inspect `*.pcap` output.

---

## Quick start

1. Make sure you have the file in your working directory 
2. Identify the interface to listen on (examples: `eth0`, `ens33`, `wlan0`).

```bash
ip link show
```

3. Run the sniffer (replace `eth0` with your interface):

```bash
sudo python3 sniffer.py -i eth0
```

4. To write captured packets to a PCAP file for later analysis:

```bash
sudo python3 sniffer.py -i eth0 -w capture.pcap
```

Open `capture.pcap` in Wireshark to inspect frames.

---

## What the output looks like

The sniffer prints one summary line per parsed IPv4 packet. Example (human-readable):

```
14:32:15 192.168.1.10 -> 93.184.216.34 proto=6 TCP 54321->80 flags=18
```

If a heuristic triggers, the sniffer prints a highlighted alert block with details, e.g.:

```
!!! SUSPICIOUS: 14:32:30 10.0.0.5 -> 172.217.164.110 proto=6 TCP 40012->80 flags=2
    >> Possible SYN-scan from 10.0.0.5 (25 SYNs in 10s)
```

**Flags** are the raw TCP flag bits. Common mapping:

* FIN = 0x001
* SYN = 0x002
* RST = 0x004
* PSH = 0x008
* ACK = 0x010
* URG = 0x020
* ECE = 0x040
* CWR = 0x080
* NS  = 0x100

---

## Heuristics and tunables

Heuristic defaults are embedded in the script (`Heuristics` class):

* **SYN detection**: `syn_threshold=20` SYNs in `syn_window=10` seconds triggers an alert.
* **DNS rate**: `dns_threshold=30` DNS requests in `dns_window=10` seconds triggers an alert.

You can adjust these by editing the `Heuristics` constructor defaults in the code to fit your lab environment.

---

## Testing ideas (safe lab)

Use a separate VM or host to generate test traffic so you do not capture other users' data.

* Simple TCP: `curl http://example.com` — should appear as TCP traffic.
* DNS traffic: `dig @8.8.8.8 example.com` repeatedly to test DNS-rate alert.
* SYN scan (lab only): from an attacker VM run `nmap -sS -p1-1000 target_ip` and watch for SYN alerts.
* Validate PCAP: open produced `capture.pcap` in Wireshark and compare parsed fields.

---

## Troubleshooting

* **No output / seeing no packets:** confirm you're bound to the correct interface and traffic exists (use `tcpdump -i <iface>` or `ip link` to verify). If the interface is down or isolated, you may not see packets.
* **Permission error:** you must run with root privileges. Use `sudo` or run as root.
* **Parsing errors / exceptions:** malformed or truncated packets can cause parsing functions to return `None`. The sniffer protects against most of these but if you see crashes, check stack trace and add defensive checks in parsing functions (bounds checking on lengths).
* **Performance issues:** single-threaded Python parsing is not high-throughput. For heavy captures, use `libpcap`-based tools or offload parsing to a separate process/thread.

---

## Security & Privacy notes for inclusion in portfolio README

* Document explicitly that this tool is for **authorized lab use only**.
* If you include sample PCAPs in the repo, sanitize them to remove private data (usernames, cookies, IPs you don’t control).
* Consider adding a short Responsible Use policy in the repo contributing guide.

