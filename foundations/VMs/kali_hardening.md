# Kali Linux Initial Hardening Guide

> A quick reference for securing a fresh Kali Linux installation. This is written with lab use in mind, but applies equally to any semi‑persistent Kali VM.

---

## 1. Accounts & Authentication

* **Change default password:**

  ```bash
  passwd
  ```
* **Create a new user (optional):**

  ```bash
  sudo adduser <username>
  sudo usermod -aG sudo <username>
  ```
* **Enable sudo logging:**

  ```bash
  sudo visudo
  # Add:
  Defaults logfile=/var/log/sudo.log
  ```

---

## 2. Updates & Package Integrity

* Update packages:

  ```bash
  sudo apt update && sudo apt full-upgrade -y
  ```
* Install unattended upgrades:

  ```bash
  sudo apt install unattended-upgrades
  sudo dpkg-reconfigure --priority=low unattended-upgrades
  ```
* Remove unused tools to reduce attack surface.

---

## 3. SSH & Remote Access

* Check SSH status:

  ```bash
  sudo systemctl status ssh
  ```
* If enabling SSH:

  ```bash
  sudo nano /etc/ssh/sshd_config
  ```

  Set:

  ```
  Port 2222
  PasswordAuthentication no
  PermitRootLogin no
  ```

  Restart:

  ```bash
  sudo systemctl restart ssh
  ```

---

## 4. Firewall / Network Hygiene

* Install & enable UFW:

  ```bash
  sudo apt install ufw
  sudo ufw default deny incoming
  sudo ufw default allow outgoing
  sudo ufw allow 2222/tcp   # if SSH is enabled on 2222
  sudo ufw enable
  sudo ufw status verbose
  ```

---

## 5. File System & Logs

* **Encryption:** If not enabled during install, consider `ecryptfs` or `gocryptfs` for sensitive data.
* **Enable auditing:**

  ```bash
  sudo apt install auditd audispd-plugins
  sudo systemctl enable --now auditd
  ```

---

## 6. Services & Persistence

* List enabled services:

  ```bash
  systemctl list-unit-files --state=enabled
  ```
* Disable unnecessary services:

  ```bash
  sudo systemctl disable bluetooth.service
  sudo systemctl disable postgresql
  sudo systemctl disable metasploit
  ```
* Check listening ports:

  ```bash
  sudo ss -tulnp
  ```

---

## 7. Additional Protections

* Install fail2ban (if exposing SSH):

  ```bash
  sudo apt install fail2ban
  ```

---

## 8. Snapshots & Backups

* In VM environments:

  * Take a snapshot after hardening.
  * Maintain a clean “gold” image separate from daily lab images.

---

## 9. Key Takeaways

* Kali is a **lab OS**, not designed as a secure daily driver.
* Harden it enough to protect your environment, but don’t treat it like a production system.
* Standard hardening flow:

  1. Change credentials / add new user
  2. Update & patch
  3. Lock down SSH or leave disabled
  4. Enable firewall
  5. Disable unneeded services
  6. Snapshot VM

---

**Author’s Note:** If you think I've missed anything please recommend further hardening techniques. I am currently using my Kali box to complete HTB labs and CTFs. This should be safe enough for HTB VPN use but I'm sure there is some paranoiac out there that will explain why I'm wrong to think that. 
