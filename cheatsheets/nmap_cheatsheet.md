# Nmap Cheatsheet

This cheatsheet covers common and useful Nmap commands for network scanning, reconnaissance, and service enumeration. Designed for practical use in security operations, CTFs, and system administration.

---

## Basic Scans

* **Ping scan (host discovery only):**

  ```
  nmap -sn 10.0.0.0/24
  ```

* **TCP connect scan (no raw packet privileges needed):**

  ```
  nmap -sT 10.0.0.5
  ```

* **SYN scan (default and faster, needs root):**

  ```
  nmap -sS 10.0.0.5
  ```

* **Scan specific ports:**

  ```
  nmap -p 22,80,443 10.0.0.5
  ```

* **Scan port ranges:**

  ```
  nmap -p 1-1000 10.0.0.5
  ```

* **Scan all ports (1–65535):**

  ```
  nmap -p- 10.0.0.5
  ```

---

## Service and Version Detection

* **Detect service versions:**

  ```
  nmap -sV 10.0.0.5
  ```

* **Enable aggressive scan (includes OS detection, version detection, script scan, traceroute):**

  ```
  nmap -A 10.0.0.5
  ```

* **Detect OS:**

  ```
  nmap -O 10.0.0.5
  ```

---

## Output Options

* **Normal output:**

  ```
  nmap -oN scan.txt 10.0.0.5
  ```

* **Grepable output:**

  ```
  nmap -oG scan.grep 10.0.0.5
  ```

* **XML output (for import into tools):**

  ```
  nmap -oX scan.xml 10.0.0.5
  ```

* **All formats at once:**

  ```
  nmap -oA scan 10.0.0.5
  ```

---

## Performance Tuning

* **Increase speed (set timing template 0–5):**

  ```
  nmap -T4 10.0.0.5
  ```

* **Minimum rate of packets per second:**

  ```
  nmap --min-rate 1000 10.0.0.5
  ```

* **Max retries per probe:**

  ```
  nmap --max-retries 2 10.0.0.5
  ```

---

## Evasion Techniques

* **Decoy scan (spoof source IPs):**

  ```
  nmap -D RND:5 10.0.0.5
  ```

* **Change source port (e.g., DNS port):**

  ```
  nmap --source-port 53 10.0.0.5
  ```

* **Fragment packets (basic firewall evasion):**

  ```
  nmap -f 10.0.0.5
  ```

* **Avoid DNS resolution:**

  ```
  nmap -n 10.0.0.5
  ```

---

## Script Scans (NSE)

* **Default scripts:**

  ```
  nmap -sC 10.0.0.5
  ```

* **Run a specific script:**

  ```
  nmap --script=http-title 10.0.0.5
  ```

* **Run scripts by category (e.g., vuln):**

  ```
  nmap --script vuln 10.0.0.5
  ```

---

## Scan Multiple Targets

* **Multiple IPs:**

  ```
  nmap 10.0.0.5 10.0.0.6
  ```

* **CIDR range:**

  ```
  nmap 10.0.0.0/24
  ```

* **From a file:**

  ```
  nmap -iL targets.txt
  ```

---

## Notes

* Use `sudo` for scans that require raw socket access.
* Be mindful of IDS/IPS alerts — some scans can be noisy.
* Scans against unauthorized systems may be illegal or against policy.

---

**Reference:** [https://nmap.org/book/man.html](https://nmap.org/book/man.html)
