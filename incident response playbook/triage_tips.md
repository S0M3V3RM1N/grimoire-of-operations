# 🛡️ Triage Tips & Tricks — A Blue Team Primer

This markdown serves as a quick-reference guide for incident responders, with a focus on fast, effective triage using open source tools. These are practical field notes — not theory, not vendor fluff.

---

## 🧭 Guiding Principles

- **Stay Calm, Move Deliberately:** Panic wastes time and leads to sloppy triage.
- **Corroborate Evidence:** Logs lie. Correlate across multiple sources before drawing conclusions.
- **Document Everything:** If it’s not written down, it didn’t happen.
- **Contain First, Understand Later:** Scope expands fast. Halt the bleeding before investigating the wound.
- **Don’t Assume Competence (or Malice):** Misconfigurations can look like compromises.

---

## 🔧 Core Tools (Open Source First)

| Tool         | Purpose                                 |
|--------------|-----------------------------------------|
| Wireshark    | Live or saved packet analysis           |
| Suricata     | IDS/IPS with rule-based alerting        |
| Zeek         | Network traffic logging and analysis    |
| Sysmon       | Detailed endpoint telemetry (Windows)   |
| OSQuery      | Endpoint state queries (cross-platform) |
| LogonTracer  | AD logon visualization from event logs  |
| KAPE         | Triage collection from Windows systems  |
| CyberChef    | Quick decoding/deobfuscation            |
| VirusTotal   | File, URL, and hash enrichment          |

---

## 📓 Triage Flow

### 1. **Initial Detection**
- Log alert, email report, user ticket, or anomaly triggers attention.
- Note time, origin, and detection method.

### 2. **Confirm the Event**
- Check source logs: firewall, EDR, mail gateway, SIEM, etc.
- Correlate across systems. Look for:
  - IPs / Timestamps
  - Process trees
  - User behavior
  - Known IOCs

> 🔍 _Tip:_ Sometimes, the EDR will trigger but the email gateway won't. Or vice versa. Trust neither alone.

### 3. **Scope It**
- Who else? What else? Lateral movement?
- Check:
  - Internal traffic to same IPs/domains
  - User account activity
  - Shared credentials or mapped drives

### 4. **Contain It**
- Isolate the host (EDR, switch port, VPN removal)
- Reset credentials
- Quarantine files / block indicators

### 5. **Document As You Go**
- Time of each action
- Tool used and findings
- Screenshots and logs saved
- Analyst notes and thoughts

---

## 🗂️ Evidence Weighing

- **Logs ≠ Truth.** Always ask: _Could this be spoofed?_ _Could this be a false positive?_
- **Email Headers:** Use multiple tools (Google Admin console, VirusTotal, header analyzers)
- **Timestamps:** Normalize timezones. A 10-second delay in a log might be 5 minutes in real time.
- **EDR Artifacts:** Don't rely on a single detection — correlate with Sysmon, Zeek, etc.

---

## 🧠 Analyst Intuition (Honed Over Time)

- Suspicious ≠ Malicious
- The weirdest alerts are often user error
- The quiet hosts are sometimes the most dangerous
- Just because it stopped doesn't mean it's over

---

## 🔚 End of Triage Checklist

- ✅ Host isolated (if needed)
- ✅ Credentials reset (if needed)
- ✅ Evidence saved (logs, PCAPs, screenshots)
- ✅ Incident report started or ticket updated
- ✅ Escalated or closed based on findings

---

> 📌 _"Triage is where intuition meets data. Log it all. Trust, but verify."_
