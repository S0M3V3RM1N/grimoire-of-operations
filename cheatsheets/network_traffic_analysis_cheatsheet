# Network Traffic Analysis Cheatsheet

> Quick reference for Blue Team defenders analyzing live traffic, PCAPs, and logs. Useful for SOC, IR, and threat hunting.

---

## 1. Common Tools

* **CLI / OS utilities**

  * `tcpdump` – packet capture, filtering.
  * `ss`, `netstat` – list active connections.
  * `iftop`, `nload` – bandwidth monitoring.
* **PCAP analysis**

  * **Wireshark** – GUI packet analysis.
  * **Zeek (Bro)** – protocol analysis + logs.
  * **Suricata** – IDS/IPS with rule-based detection.
* **Flow/Logs**

  * NetFlow/IPFIX collectors.
  * Firewall, proxy, and DNS logs.

---

## 2. Key Protocols & Indicators

* **DNS**

  * Long/encoded queries → possible tunneling.
  * High entropy subdomains (DGAs).
* **HTTP/HTTPS**

  * Suspicious User-Agent or rare headers.
  * JA3/JA3S mismatches (TLS fingerprint anomalies).
  * TLS without SNI or self-signed certs.
* **ICMP**

  * Large/fragmented payloads → tunneling.
* **Other**

  * SMB/RDP/SSH unusual external traffic.
  * Non-standard ports running known services.

---

## 3. Quick tcpdump Filters

```bash
# Capture traffic to/from an IP
sudo tcpdump -i eth0 host 10.10.10.10

# Capture DNS queries
sudo tcpdump -i eth0 port 53

# Capture HTTP GET/POST
sudo tcpdump -i eth0 -A -s 0 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'

# Capture only TCP SYN packets (scan detection)
sudo tcpdump 'tcp[13] & 2 != 0'
```

---

## 4. Zeek Log Fields to Watch

* **conn.log** → duration, orig\_bytes vs resp\_bytes.
* **dns.log** → query length, uncommon TLDs.
* **ssl.log** → ja3, cert subject/issuer.
* **http.log** → user\_agent, method, status\_code.

---

## 5. Hunting Queries (ELK/SIEM style)

* **Beaconing (regular intervals)**

```sql
SELECT src_ip, dst_ip, COUNT(*) as hits, ROUND(AVG(duration),2) as avg_dur
FROM conn
GROUP BY src_ip, dst_ip
HAVING hits > 20 AND avg_dur < 60;
```

* **Large outbound transfers**

```sql
SELECT src_ip, SUM(bytes_out)
FROM flows
GROUP BY src_ip
HAVING SUM(bytes_out) > 100000000; -- ~100MB
```

---

## 6. Common Red Flags

* Connections to IPs with no reverse DNS.
* TLS without SNI or with rare cipher suites.
* Multiple failed connections before success.
* Sudden spike in DNS TXT or MX queries.
* Hosts communicating on ports not whitelisted for business.

---

## 7. MITRE ATT\&CK Mapping (Network Focus)

* **T1071** – Application Layer Protocol (HTTP/HTTPS/DNS/SMTP).
* **T1095** – Non-Application Layer Protocol.
* **T1041** – Exfiltration over C2 Channel.
* **T1573** – Encrypted Channel (non-standard port).
* **T1568** – Dynamic Resolution (DNS-based).

---

## 8. Workflow Checklist

1. Identify scope: IPs, users, timeframe.
2. Collect PCAP/flows/logs.
3. Baseline vs anomaly comparison.
4. Pivot on suspicious indicators (JA3, domains, ports).
5. Extract IOCs for enrichment (VT, threat intel).
6. Document findings + containment recommendations.

---

## 9. References

* [Zeek Documentation](https://docs.zeek.org/)
* [Suricata Rules Guide](https://suricata.readthedocs.io/en/latest/)
* [Wireshark Display Filters](https://wiki.wireshark.org/DisplayFilters)
* [MITRE ATT\&CK](https://attack.mitre.org/)

---
