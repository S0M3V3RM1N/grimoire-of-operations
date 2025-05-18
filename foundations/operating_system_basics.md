# Operating System Basics for Security Professionals

> Understanding how an operating system (OS) works isn't optional. It's core knowledge — whether you're in security, helpdesk, sysadmin, or trying to get your first SOC job. Every process, every log, every vulnerability comes down to how the OS handles instructions, memory, and users. 

---

## What Is an Operating System?

An operating system is the bridge between the hardware and the user. It manages system resources like CPU, memory, storage, and input/output devices. Without it, your system is a useless pile of components.

There are three major families most security folks deal with:

- **Windows** — Common in enterprise environments. Heavily targeted by malware and threat actors.
- **Linux/Unix-like** — Runs the internet. Also used in most security tools and infrastructure.
- **macOS** — Less common in enterprise, but still relevant. Built on Unix principles.

---

## Core Components

- **Kernel**  
  The heart of the OS. Handles communication between hardware and software.

- **Processes and Threads**  
  Anything running on the OS is a process. Each process can have multiple threads. You need to understand this when hunting for malware or tuning performance.

- **Memory Management**  
  Determines how RAM is allocated to processes. Important for recognizing memory corruption attacks (like buffer overflows).

- **File System**  
  Defines how files are stored and retrieved. Linux uses ext4, Windows uses NTFS. Know where system files live and what normal vs. suspicious looks like.

- **User and Permission Models**  
  Who can do what. File permissions, user groups, privilege escalation — this is a goldmine for attackers if misconfigured.

- **System Calls and APIs**  
  The methods programs use to ask the OS for resources. Red teamers abuse these, and blue teamers catch it in logs.

---

## Why This Matters in Security

### 📍 1. Threats Live on the OS  
Malware, backdoors, rootkits — they all run on top of or beneath the OS layer. You can't defend what you don't understand.

### 🔍 2. Logs and Artifacts Come From the OS  
Event Viewer, journald, auth.log, syslog — all of these come from the OS. Your ability to triage an incident often starts with knowing which log to look at.

### 🛠 3. Defensive Tools Interact With the OS  
EDR, AV, firewalls, SIEM agents — they rely on OS-level hooks. Understanding how these tools work requires understanding the OS internals.

### 🚩 4. Attackers Abuse Native Functions  
PowerShell, WMI, cron, scheduled tasks — these are normal admin tools used maliciously. If you don’t know what “normal” is, you won’t spot “weird.”

---

## Key Things to Practice

- Navigate both **Windows (CMD/PowerShell)** and **Linux (bash)** from the command line
- Understand **file structures** (`C:\Windows\System32` vs `/etc`, `/var/log`)
- Know how to view and manage **processes**, **users**, and **permissions**
- Be able to read **basic logs** and understand what they’re telling you
- Learn to install, run, and troubleshoot **basic services** (SSH, web servers, etc.)

---

## Resources to Learn More

- [OverTheWire: Bandit](https://overthewire.org/wargames/bandit/)
- [Windows Command Line Crash Course](https://learn.microsoft.com/en-us/windows/terminal/)
- [Linux Journey](https://linuxjourney.com/)
- [Malware Unicorn’s Windows Internals](https://malwareunicorn.org/workshops/#windows-internals)

---

## Final Note

Every click, every breach, every log entry starts with an OS doing what it was told to do. Mastering the basics here will give you the edge in almost every area of IT and security. You don’t need to memorize everything — but you do need to be comfortable poking around, breaking things, and figuring out how it all fits together.

