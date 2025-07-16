**Purpose**: This is a cheatsheet that covers commonly used PowerShell commands for system management, file manipulation, network inspections, auditing, and scripting basics. Useful for incident responders, defenders, and IT professionals

---

### Basics
```
# Launch PowerShell
powershell

# Get PowerShell version
$PSVersionTable

# Get help for a command
Get-Help Get-Process
Get-Help Get-Process -Examples

# List available commands
Get-Command
```
---

### File and Directory

```
# List contents of directory
Get-ChildItem
ls     # alias

# Change directory
Set-Location C:\Logs
cd C:\Logs    # alias

# Copy file
Copy-Item .\file.txt C:\Backup\file.txt

# Move file
Move-Item .\file.txt C:\Backup\

# Delete file
Remove-Item .\file.txt
```
---

### System Info

```
# List processes
Get-Process

# Kill a process
Stop-Process -Name notepad

# System info
Get-ComputerInfo

# Services
Get-Service
Start-Service -Name spooler
Stop-Service -Name spooler
```
---

### Network

```
# IP configuration
Get-NetIPAddress

# View open TCP connections
Get-NetTCPConnection

# Test network connectivity
Test-Connection 8.8.8.8
Test-NetConnection google.com -Port 443
```
---

### Security / Users

```
# List users
Get-LocalUser

# Add new user
New-LocalUser "username" -Password (Read-Host -AsSecureString)

# List local groups
Get-LocalGroup

# Add user to group
Add-LocalGroupMember -Group "Administrators" -Member "username"

# View event logs (System, Application, Security)
Get-EventLog -LogName Security -Newest 20
```
---

### Files & Forensics

```
# Get file hash (for integrity checking)
Get-FileHash .\suspect.exe -Algorithm SHA256

# Search for a string in files
Select-String -Path *.log -Pattern "failed login"

# List all scheduled tasks
Get-ScheduledTask
```
---

### Script Control and Execution

```
# View current execution policy
Get-ExecutionPolicy

# Temporarily allow script execution
Set-ExecutionPolicy Bypass -Scope Process

# Run a script
.\script.ps1
```
---

### Useful Shortcuts & Aliases

| Alias | Full Cmd      |
| ----- | ------------- |
| `ls`  | Get-ChildItem |
| `cd`  | Set-Location  |
| `mv`  | Move-Item     |
| `cp`  | Copy-Item     |
| `rm`  | Remove-Item   |
| `cat` | Get-Content   |

