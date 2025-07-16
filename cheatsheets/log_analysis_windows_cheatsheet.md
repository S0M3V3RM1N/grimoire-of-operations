## Windows Log Analysis Cheatsheet

> **Purpose**: This cheatsheet focuses on Windows log sources and common techniques used in security monitoring and investigation. Use this to assist with triage, threat hunting, or forensic analysis.

---

### Key Windows Log Sources

#### Event Viewer Logs

* **Application**: Application-level events
* **System**: Operating system and driver events
* **Security**: Authentication, authorization, object access
* **Setup**: Installation and setup events
* **Forwarded Events**: Events collected from remote systems

**Log Path:** `C:\Windows\System32\winevt\Logs`

---

### Key Event IDs (Security Log)

| Event ID | Description                        |
| -------- | ---------------------------------- |
| 4624     | Successful logon                   |
| 4625     | Failed logon                       |
| 4634     | Logoff                             |
| 4648     | Logon with explicit credentials    |
| 4672     | Admin privileges assigned          |
| 4688     | Process created                    |
| 4689     | Process ended                      |
| 4697     | Service installed                  |
| 4720     | User account created               |
| 4722     | User account enabled               |
| 4723     | Password change attempted          |
| 4724     | Password reset attempted           |
| 4725     | User account disabled              |
| 4726     | User account deleted               |
| 4768     | Kerberos TGT requested             |
| 4769     | Kerberos service ticket requested  |
| 4771     | Kerberos pre-auth failed           |
| 4798     | User's group membership enumerated |

---

### Tools for Log Analysis

* **Event Viewer**: GUI log inspection
* **Get-WinEvent**: PowerShell cmdlet to query logs
* **wevtutil**: CLI tool for log management
* **Sysmon**: Extended event logging via Sysinternals
* **LogParser**: Microsoft CLI for querying logs
* **Windows Event Forwarding (WEF)**: Centralized collection
* **Velociraptor / Kape / Sigma Rules**: Threat hunting tools

---

### PowerShell Examples

```powershell
# Query 4625 failed logons from Security log
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} | Format-Table -AutoSize

# Search for a specific user login
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624} | Where-Object { $_.Message -like '*jdoe*' }

# Count number of failed logons
(Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625}).Count
```

---

### Things to Watch For

* Multiple 4625 (failed logon) entries from same IP
* Privilege escalation indicators (4672, 4728, 4732)
* Abnormal process creation (4688)
* Execution from uncommon directories (e.g., temp folders)
* Scheduled task creation or modification
* New service installation (4697)
* Logon types (type 3 = network, type 10 = RDP)
* Time-of-day anomalies (logons during off-hours)

---

### Logon Types

| Type | Description               |
| ---- | ------------------------- |
| 2    | Interactive (local login) |
| 3    | Network (e.g., SMB login) |
| 4    | Batch                     |
| 5    | Service                   |
| 7    | Unlock workstation        |
| 10   | Remote Interactive (RDP)  |
| 11   | Cached interactive logon  |
