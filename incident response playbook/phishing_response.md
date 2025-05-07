# Phishing Response Plan

## Summary
Step-by-step guide for analyzing reported phishing emails, identifying affected users, and remediating account compromise within a Google Workspace environment.

---

## 1. Email Triage

**Tools Used:**
- Gmail headers → VirusTotal (header/IP/domain reputation)
- Falcon Insights sandbox (link/attachment behavior analysis)

**Checklist:**
- [ ] Confirm phishing indicators (spoofed sender, obfuscated links, urgency tactics)
- [ ] Extract URLs and attachments
- [ ] Submit to VirusTotal or sandbox for verdict

---

## 2. Investigate Impact Scope

**Tools Used:**
- Google Admin Investigation Tool

**Steps:**
- Search for the subject line or sender domain across the org
- Identify all recipients
- Check which users clicked links (click-tracking in Admin panel)

---

## 3. Incident Response Actions

**User Clicked?**
- [x] Immediately notify user to reset password
- [x] Clear active sessions (Google Admin > User > Security)
- [x] If no contact can be made, account suspension until confirmed password resets. 

---

## 4. Post-Incident

**Tracking/Logging Steps:**
- Tag incident in log (see `incident_log_template.md`)
- Submit sender domain/IP to allow/blocklist (if authorized)
- Document patterns (for playbook update)

---

## Notes:
- If multiple users clicked, treat as active campaign
- Track phishing themes for behavioral trends
- Indetify new techniques used by threat actors
- Report malicious domains to service providers
