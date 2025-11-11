# Kill Chain Framework

The **Lockheed Martin Cyber Kill Chain®** outlines the sequence of steps adversaries typically follow to conduct a successful cyber-attack. Understanding each phase empowers defenders to disrupt intrusions—often before significant damage occurs. While linear, this framework is foundational for threat hunting, SOC analysis, and incident response.

---

## The 7 Stages (with Defender Strategies)

| Stage                 | Attacker Actions                                             | Detection/Prevention Strategies                                   |
|-----------------------|-------------------------------------------------------------|-------------------------------------------------------------------|
| **1. Reconnaissance** | Collect target info, probe infrastructure                   | Monitor OSINT, suspicious scanning, threat intelligence           |
| **2. Weaponization**  | Develop exploit, couple with delivery payload               | Threat intel feeds, automated sandboxing, YARA rules              |
| **3. Delivery**       | Transmit malicious payload to target                        | Email/web filtering, endpoint monitoring                          |
| **4. Exploitation**   | Execute exploit code, leverage vulnerabilities/user errors  | Patch management, restrict macros, alert on exploit attempts      |
| **5. Installation**   | Install malware/persistence mechanisms                      | EDR, autorun config policy, file integrity checks                 |
| **6. Command & Control (C2)** | Establish remote control over asset             | Network monitoring, DNS/proxy logs, block known C2 infrastructure |
| **7. Actions on Objectives** | Data theft, lateral movement, sabotage            | DLP, alarms for privilege escalation/lateral movement             |

---

### Stage Details

**1. Reconnaissance**  
Adversaries **gather intelligence**: identifying people, infrastructure, exposed services (web apps, VPN, email portals), passwords on breach sites, social media, and more.  
- **Modern Risk:** Cloud misconfigurations, credential leaks.  
- **SOC Tip:** Automate monitoring for company-related leaks, domain name use, and web scans.

**2. Weaponization**  
Attacker develops malicious payloads (e.g. malware, exploit documents, phishing kits) tailored to the target’s tech stack and environment.  
- **Gap:** Defenders rarely see this phase unless engaged in deep threat intel or malware research.  
- **SOC Tip:** Collaborate with threat intel, automate sample collection/sandboxing.

**3. Delivery**  
Transmitting the payload: email (phishing), cloud shares, USB, drive-by downloads, supply chain compromise, social engineering.  
- **Modern Risk:** Cloud file sharing, QR-code phishing, SMS attacks.  
- **SOC Tip:** Layered filtering/inspection (SEG, proxy, browser isolation).

**4. Exploitation**  
Payload activates by leveraging tech flaw (e.g. CVE) or user action (macro, credential entry).  
- **Gap:** Zero-days or unpatched assets.  
- **SOC Tip:** Prioritize patching, enforce least privilege, monitor exploit behavior.

**5. Installation**  
Malware or backdoor gains persistence: registry keys, scheduled tasks, WMI, browser extensions, or cloud OAuth tokens.  
- **Modern Risk:** Fileless malware, cloud persistence, living-off-the-land techniques.  
- **SOC Tip:** Monitor for new persistence techniques (autoruns, startup folders, OAuth grants).

**6. Command & Control (C2)**  
Attacker establishes outbound comms (DNS tunneling, HTTPS callbacks, cloud-based C2, Telegram, Slack, Discord).  
- **Gap:** Encrypted traffic, stealthy beaconing, legit platforms (e.g., Gmail for C2).  
- **SOC Tip:** Traffic anomaly detection, threat feeds for C2 hosts, decrypt SSL/TLS if possible.

**7. Actions on Objectives**  
Final goal: exfiltration, ransomware, destruction, privilege escalation, data manipulation, lateral movement.  
- **Modern Risk:** Multi-stage ransomware, blending exfil/impact, cloud-native attacks.  
- **SOC Tip:** DLP, privilege monitoring, lateral movement tracing, SIEM behavioral alerts.

---

## Practitioner Guidance

- **Break the Chain Early:** Prevention/detection at *any stage* can foil the attack. Focus on the earliest phase possible.
- **Layered Defenses:** Overlapping controls (defense in depth), especially for reconnaissance, delivery, and exploitation.
- **Routine Tabletop Exercises:** Map real incidents to the Kill Chain, refine hunt/response playbooks.
- **Use in Hunting:** Proactively hunt for attacker artifacts per stage—unusual recon, delivery attempts, C2 traffic.

---

## Contemporary Considerations

- **Non-Linear Attacks:** Modern adversaries may skip or blend stages, revisit earlier phases, or operate long “dwell times.”
- **Cloud & SaaS:** Kill Chain logic applies to on-prem, cloud, and hybrid threats—adjust monitoring accordingly.
- **Kill Chain + ATT&CK:** Use Kill Chain for strategic mapping (incident timelines, detection coverage), ATT&CK for tactical TTPs and enrichment.

---

## Frameworks to Compare

- **MITRE ATT&CK:** Rich, granular coverage of techniques; better for hunt/response.  
- **Diamond Model:** Emphasizes adversary relationships and infrastructure.  
- **D3FEND:** Defensive technique mapping—pair with ATT&CK for blue-team efficacy.

---

**Further Reading & Resources:**
- [Lockheed Martin Cyber Kill Chain®](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [SANS Hunt Evil](https://www.sans.org/blog/the-threat-hunting-maturity-model/)

