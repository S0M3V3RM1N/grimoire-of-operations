# Network Fundamentals for Security Operators

This page is a brief breakdown of the networking knowledge needed to find success in a career in cybersecurity, administration, and network infrastructure. This is not a copy & paste from online resources. Instead, this document is intended to be a **quick reference or review** of what you may already know — or to help you form the right questions to research further.

Networking is a beast. So is security. Both are deep, layered, and never finished. You don’t need to be a CCNA to break into security, but understanding how data moves across a network is **non-negotiable**. This guide focuses on that — not passing a test, but gaining clarity.

---

## 🧱 Core Concepts

### IP Addresses
Think of IPs like mailing addresses. Devices need them to send and receive data. There are two types:
- **IPv4** (e.g., `192.168.1.10`)
- **IPv6** (e.g., `2001:0db8:85a3::8a2e:0370:7334`)

Security Relevance:
- Know how to trace internal vs external IPs during an investigation.
- Understand how spoofed IPs or private IPs behave in logs.

---

### Subnetting
This defines how big your local network is. It tells devices if another IP is nearby (local) or far away (needs routing).

Security Relevance:
- Helps determine lateral movement scope.
- Useful for narrowing threat detection zones in SIEMs.

---

### MAC Addresses
Hardware-level addresses burned into NICs. Layer 2 identifiers.

Security Relevance:
- Shows up in switch logs and ARP tables.
- Can be spoofed in attacks (e.g., MAC flooding, impersonation).

---

### Ports & Protocols
Data flows through specific **ports** using **protocols** (rulesets). Examples:
- **TCP/UDP ports**: 80 (HTTP), 443 (HTTPS), 22 (SSH), 53 (DNS)
- **Common protocols**: DNS, DHCP, HTTP/S, FTP, ICMP

Security Relevance:
- Know your well-known ports.
- Helps spot suspicious connections (e.g., RDP on non-standard ports, DNS tunneling).

---

### OSI Model (7 Layers)
A conceptual model for how data moves through a network.

From top (Layer 7) to bottom (Layer 1):
- Application
- Presentation
- Session
- Transport
- Network
- Data Link
- Physical

Security Relevance:
- Useful for pinpointing where an attack occurs (e.g., ARP spoofing = Layer 2, DDoS = Layer 3-4).
- Helps when analyzing packet captures or firewall rules.

---

### VLANs & Trunking
**VLANs** segment broadcast domains at Layer 2. **Trunking** allows multiple VLANs over one link.

Security Relevance:
- Know how VLAN misconfigurations lead to lateral movement.
- VLAN hopping is a common Layer 2 attack.

---

### Routing
Routers connect different networks and decide where traffic goes.

Security Relevance:
- Understand the difference between internal routing and internet-bound traffic.
- Routes can be hijacked (BGP attacks) or misconfigured (route leaks).

---

### NAT (Network Address Translation)
Translates private IPs to public ones (and back). Used heavily in firewalls.

Security Relevance:
- Makes attribution harder — many internal IPs may appear as one.
- Important when analyzing firewall logs.

---

### DNS (Domain Name System)
Translates domains to IP addresses.

Security Relevance:
- Common attack vector (e.g., DNS hijacking, tunneling).
- DNS logs can reveal C2 infrastructure.

---

### ARP (Address Resolution Protocol)
Maps IPs to MAC addresses on local networks.

Security Relevance:
- ARP poisoning = common man-in-the-middle attack.
- Crucial for packet analysis at Layer 2.

---

## 🔍 For Security Operators

- Learn to **read packet captures** (Wireshark, tcpdump).
- Understand **log sources** (firewall, switch, DNS, DHCP).
- Know how to **trace a threat across layers** (from endpoint to edge).
- Practice **building and breaking** basic network setups — even in a lab VM.

---

## 🧠 Final Note

This isn’t meant to be your final form — it’s meant to spark your curiosity. If you don’t know what something means, don’t skip it. **Chase it.** Write it down. Break it apart. That’s how you get dangerous.

*"Security without networking is like a lock without a door — you’re missing the point."*

