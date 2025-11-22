# Wireshark and Network Traffic Analysis: Foundations for Blue Team Operations

Network traffic analysis is one of the most reliable ways to confirm what actually happened on a system. Logs can be incomplete, hosts can be tampered with, but packets tell the truth. Wireshark remains the primary tool for deep inspection because it gives analysts full visibility into the structure, timing, and content of the raw traffic moving across a network.

This document covers the core concepts and workflows a blue team operator should understand when working with Wireshark to perform network traffic analysis.

---

## 1. Understanding What Traffic Tells You

Network traffic answers questions about activity and is an essential in proper triage. With the right view, you can determine:

* Which hosts communicated and when
* What protocols and ports were used
* Whether authentication took place
* Indicators of command execution or lateral movement
* Data flow direction and volume
* Potential exfiltration patterns
* Unusual service usage or failed connection attempts

A large part of traffic analysis is identifying what does not belong within normal patterns.

---

## 2. Building Effective Filters

Wireshark supports Berkeley Packet Filter (BPF) syntax and its own display filters. Knowing how to filter quickly is essential for eliminating noise.

Common foundational filters:

**Host-based filters**

```
ip.addr == 192.168.1.50
ip.src == 192.168.1.50
ip.dst == 192.168.1.50
```

**Port-based filters**

```
tcp.port == 445
udp.port == 53
```

**Protocol filters**

```
tcp
udp
dns
http
tls
rdp
icmp
```

**Conversation isolation**

```
tcp.stream eq 5
```

**Highlighting anomalies**

```
tcp.flags.syn == 1 and tcp.flags.ack == 0
// SYNs
tcp.flags.reset == 1
// RST storms or failed connections
```

Filtering is how you convert a 50,000-packet capture into a 50-packet problem.

---

## 3. Following the Flow: TCP and Application Layer Behavior

Blue team operators should be able to read:

* TCP three-way handshakes to confirm successful or failed connections
* SYN floods, repeated retries, and abnormal resets
* Session establishment for protocols like RDP, SMB, SSH, and HTTPS
* Unexpected beaconing patterns at precise intervals
* Unusual client behavior, such as a workstation initiating outbound SMB

Understanding how normal connections look makes anomalies obvious.

---

## 4. TLS Decryption for Legitimate Investigations

If you have lawful access to:

* A server’s private key (RSA-based key exchange)
* Session keys (exported from endpoints using SSLKEYLOGFILE)

you can decrypt TLS traffic inside Wireshark to reveal:

* HTTP requests and responses
* Credentials passed in poorly designed apps
* Metadata used for lateral movement
* RDP security negotiations
* Indicators of malware command channels

Note: TLS decryption requires proper key material and cannot be brute-forced or guessed. Modern TLS 1.3 requires endpoint session keys rather than server private keys.

---

## 5. Identifying Malicious Activity in Packet Captures

Key signs a blue team operator should be looking for:

### Authentication Abuse

* Repeated failed logins
* SMB or RDP brute forcing
* Credential reuse across hosts

### Lateral Movement Indicators

* Unexpected RDP sessions
* New SMB connections to unusual hosts
* Remote service creation
* New administrator accounts visible inside command output

### Command-and-Control

* Beaconing at steady intervals
* Uncommon protocols for the environment
* Traffic leaving the network toward VPS-like IP ranges

### Data Exfiltration

* High-volume outbound transfers
* Staging behavior on internal servers
* DNS tunneling patterns

Packets form a timeline of malicious behavior in a way that logs sometimes miss.

---

## 6. Baseline First, Investigate Second

Baselining is non-negotiable. If you understand:

* Normal DNS patterns
* Standard ports used by internal systems
* Expected authentication flows
* Regular update cycles
* Normal device-to-device talk

then anomalies jump off the screen.

Wireshark is not just for deep dives. It is a validation tool for what normal actually looks like.

---

## 7. Documenting Your Findings

Good incident responders document:

* Timeframes observed
* Hosts involved
* Packet numbers for key events
* Streams that show suspicious activity
* Exact queries, commands, or actions the attacker performed
* Whether the traffic indicates foothold, privilege escalation, lateral movement, or exfiltration

Your analysis should be reproducible by another responder without guessing.

---

## 8. When Wireshark Is the Right Tool

Wireshark excels when:

* You need to confirm what happened across the wire
* You need to analyze malware-infected traffic manually
* You want to validate IDS or SIEM alerts
* Logs are incomplete or have been wiped
* You need high-fidelity visibility into authentication or handshakes
* You need to validate encryption, tunneling, or suspicious sessions

Wireshark is not a full IR platform, but it is the microscope every blue team should know how to use.

---

## Final Notes

Traffic analysis is a core skill that pays off in every area of defensive security. The more comfortable you become with protocol behavior, filtering, and following conversations, the faster you can identify what is normal and what is a threat.
