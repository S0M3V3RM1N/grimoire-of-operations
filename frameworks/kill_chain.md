# Kill Chain Framework

The **Lockheed Martin Cyber Kill Chain®** is one of the earliest formalized models for understanding how cyber intrusions unfold. It breaks an attack down into discrete phases, helping defenders think proactively: **Where in the chain can we detect, disrupt, or deny the adversary?**

Though more linear than frameworks like MITRE ATT&CK, the Kill Chain still serves as a solid strategic lens — especially when crafting detection logic or reviewing incident timelines.

---

## 🧩 The 7 Stages

1. **Reconnaissance**  
   Adversary profiles targets and gathers information (emails, infrastructure, exposed services).
   - 🔍 Examples: DNS harvesting, social media mining, Shodan scans
   - 🛡️ Defenders: Monitor for passive scans, OSINT mentions, watering hole setups

2. **Weaponization**  
   A payload is paired with a delivery mechanism — the attacker creates the tool.
   - 💣 Examples: Macro-enabled document, exploit-laden PDF, Trojaned installer
   - 🛡️ Defenders: Limited visibility unless threat intel or sandboxing is involved

3. **Delivery**  
   Payload reaches the target.
   - ✉️ Examples: Phishing email, malicious USB, drive-by download
   - 🛡️ Defenders: Email filters, proxy inspection, endpoint controls

4. **Exploitation**  
   The code executes by exploiting a vulnerability or user error.
   - 🐛 Examples: CVE abuse, macro execution, default creds
   - 🛡️ Defenders: Patch management, privilege limits, macro restrictions

5. **Installation**  
   Malware or access mechanism is installed on the system.
   - ⚙️ Examples: Remote access tools (RATs), rootkits, persistence registry keys
   - 🛡️ Defenders: EDR alerts, autorun configs, file integrity monitoring

6. **Command & Control (C2)**  
   Attacker establishes outbound communication.
   - 📡 Examples: DNS tunneling, HTTPS callbacks, social media channels
   - 🛡️ Defenders: DNS logging, proxy alerts, beacon pattern detection

7. **Actions on Objectives**  
   The endgame: data theft, encryption, lateral movement, destruction.
   - 🎯 Examples: Ransomware detonation, database exfil, sabotage
   - 🛡️ Defenders: DLP alerts, anomalous behavior, lateral movement tracing

---

## 📌 Why It Still Matters

- **Detection Coverage**: Helps structure alerting and detection logic by attack stage.
- **Incident Review**: Useful for reconstructing timelines during investigations.
- **Threat Modeling**: Helps identify which parts of the chain your org is weak at.

---

## 🧠 Compare With

- **MITRE ATT&CK**: More granular and behavior-focused; Kill Chain is strategic, ATT&CK is tactical.
- **Diamond Model**: Focuses on relationships (adversary, infrastructure, victim, capability).
- **D3FEND**: Blue-team mirror of ATT&CK with defensive techniques.

---

*"Every chain has a weakest link. Make sure it’s the attacker’s, not yours."*

