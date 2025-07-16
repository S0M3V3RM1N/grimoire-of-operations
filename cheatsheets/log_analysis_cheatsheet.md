## Log Analysis Cheatsheet

> **Purpose**: This cheatsheet offers a reference for analyzing system, application, and network logs during security investigations, audits, or general system administration. Use it to spot anomalies, detect suspicious activity, and reconstruct events.

---

### Common Log File Types and Locations

#### Linux

```
/var/log/syslog              # General system activity (Debian/Ubuntu)
/var/log/messages            # General system activity (RHEL/CentOS)
/var/log/auth.log            # Authentication logs
/var/log/secure              # Security/auth logs (RHEL)
/var/log/cron                # Cron jobs
/var/log/kern.log            # Kernel logs
/var/log/dmesg               # Boot and hardware messages
/var/log/apache2/access.log  # Web server access
/var/log/apache2/error.log   # Web server errors
```

#### Windows

```
Windows Event Viewer:
- Application Logs
- Security Logs
- System Logs

Log location: C:\Windows\System32\winevt\Logs

Use `Get-WinEvent` or `wevtutil` to query logs programmatically.
```

---

### Techniques & Filters

#### Basic Grep Usage

```bash
grep 'keyword' logfile.log
grep -i 'login failed' auth.log    # case-insensitive
```

#### Combine with other commands

```bash
cat /var/log/auth.log | grep 'sshd' | grep 'Failed password'
```

#### Use `awk` or `cut` to extract fields

```bash
awk '{print $1, $2, $3}' /var/log/auth.log
cut -d ' ' -f 1-3 /var/log/auth.log
```

---

### Things to Look For

* Repeated failed logins
* Login attempts from unusual IPs or geo-locations
* New user accounts or privilege changes
* Unexpected software installations or service changes
* Outbound connections to known bad IPs/domains
* Sudden spikes in traffic or CPU/memory
* Scheduled tasks or cron jobs added/modified
* Base64, PowerShell, or encoded strings in logs

---

### Useful Tools

* `journalctl` (systemd-based Linux distros)
* `ausearch` / `auditctl` (Linux AuditD)
* `LogParser` (Windows)
* `Sysmon` + `LogonTracer`
* `Grep`, `awk`, `sed`, `cut`, `uniq`, `sort`
* ELK Stack (Elasticsearch, Logstash, Kibana)
* Graylog

---

### Sample Log Entries

**Failed SSH login:**

```
Jul 15 10:32:41 server sshd[10012]: Failed password for invalid user admin from 192.168.1.22 port 51234 ssh2
```

**Cron Job:**

```
Jul 15 03:01:01 server CRON[1234]: (root) CMD (/usr/local/bin/backup.sh)
```

**Windows Security Log (Event ID 4624 - Successful Logon):**

```
An account was successfully logged on.
  Subject:
    Security ID:        SYSTEM
    Account Name:       WIN-123456\SYSTEM
    Logon ID:           0x3e7
  Logon Type:           2
  New Logon:
    Security ID:        WIN-123456\User1
```
