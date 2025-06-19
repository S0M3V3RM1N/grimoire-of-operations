# 🧩 Common Windows Event IDs for DFIR and Threat Hunting

This document outlines **critical Windows Event IDs** used in digital forensics, incident response (DFIR), and threat hunting. It is focused on **high-fidelity telemetry**, relevant log artifacts, and correlated threat behaviors. Each event is triple-checked against Microsoft documentation and known detection engineering practices.

---

## 🔐 Authentication & Logon Events

| Event ID | Log Source     | Description |
|----------|----------------|-------------|
| **4624** | Security        | Successful logon (Check Logon Type: 10 = RDP, 3 = Network) |
| **4625** | Security        | Failed logon attempt |
| **4648** | Security        | Logon using explicit credentials (e.g., `runas`, pass-the-hash) |
| **4672** | Security        | Special privileges assigned to new logon (Admin-equivalent) |

---

## 🧠 User Behavior & Lateral Movement

| Event ID | Log Source     | Description |
|----------|----------------|-------------|
| **4688** | Security        | New process created (Command line args crucial) |
| **4697** | Security        | New service installed (Can indicate persistence) |
| **7045** | System          | Service installation (Redundant with 4697, more details) |
| **4649** | Security        | A replay attack was detected (rare, but useful) |

---

## 🛠 PowerShell & Script Execution

> Requires advanced logging: **Script Block Logging**, **Module Logging**, and **Process Creation Logging** via GPO/Sysmon.

| Event ID | Log Source     | Description |
|----------|----------------|-------------|
| **4104** | Microsoft-Windows-PowerShell/Operational | PowerShell script block logging (shows decoded script content) |
| **4103** | Microsoft-Windows-PowerShell/Operational | PowerShell command invocation |
| **4688** | Security        | Process creation (catch `powershell.exe`, `cmd.exe`, `wscript.exe`) |
| **800**  | PowerShell      | PowerShell engine started (older log, low fidelity) |

---

## 📁 File, Registry, and Object Access

> Enable "Audit Object Access" in local or domain policy for these to be logged.

| Event ID | Log Source     | Description |
|----------|----------------|-------------|
| **4657** | Security        | Registry value modified |
| **4663** | Security        | File accessed (check for sensitive paths like `LSASS`, `SAM`, etc.) |
| **4698** | Security        | Scheduled task created (Persistence indicator) |

---

## 🔄 Network & Remote Access

| Event ID | Log Source     | Description |
|----------|----------------|-------------|
| **5156** | Security (Filtering Platform) | Allowed network connection |
| **5158** | Security (Filtering Platform) | Bound to a port for listening |
| **4776** | Security        | Credential validation (especially for Kerberos) |
| **4769** | Security        | Kerberos service ticket request (TGS — used in lateral movement)

---

## 🧰 Useful Sysmon Events (If Installed)

| Event ID | Description |
|----------|-------------|
| **1**    | Process creation (CommandLine, Hashes, Parent) |
| **3**    | Network connection (source/dest IP, port) |
| **11**   | File creation (track dropped payloads) |
| **13**   | Registry value set (persistence indicators) |
| **7**    | Image load (DLLs) |

---

## 🔎 Hunting Notes
- **Logon Type 10** on Event 4624 = RDP
- **Event ID 4688** is critical: use command line + parent-child relationships
- **PowerShell abuse often begins with -EncodedCommand, IEX, or WebClient**
- Correlate **4624** (logon), **4688** (execution), and **4104** (script) for timeline reconstruction

---

## 🗂️ Resources
- [Microsoft Security Auditing Event ID Documentation](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/basic-security-audit-events)
- [Sigma Rules for Windows](https://github.com/SigmaHQ/sigma)
- [SwiftOnSecurity’s Sysmon Config](https://github.com/SwiftOnSecurity/sysmon-config)

---

_Updated: June 2025 — Verified against live blue team lab analysis and Microsoft documentation._
