# 🧑‍💻 Account Compromise Response Plan

## Summary

This playbook outlines the steps taken when a user account is suspected or confirmed to be compromised. The response prioritizes containment, communication, and credential recovery, with actions tailored to a Google Workspace environment.

---

## 1. Indicators of Compromise

Common triggers for this workflow:
- User clicked a known phishing link
- External alert 
- Unexpected login location or device
- Abnormal behavior observed by support or reported by user

---

## 2. Containment Actions

**If a compromise is suspected:**

- [ ] Search for recent login activity
- [ ] Verify whether login occurred from unauthorized regions or devices
- [ ] If suspicious, proceed with user lockout:
  - Suspend the account
  - Revoke all active sessions
  - Remove app tokens (especially OAuth scopes)

---

## 3. User Coordination

- [ ] Notify the user via alternate contact (phone, onsite)
- [ ] Instruct user to:
  - Reset their password (enforce strong password policy)
  - Verify recovery options
  - Report any unusual activity
- [ ] Provide a quick security hygiene checklist if applicable
- [ ] Check for any changes made to account settings or email filters

**If the user is unresponsive:**
- [x] Keep account suspended until direct contact is made

---

## 4. Post-Compromise Review

- [ ] Review MFA sign-in logs.
- [ ] Search logs for any sensitive data access or file shares during the compromise window
- [ ] Notify relevant stakeholders (if policy requires)
- [ ] Document the incident using the log template

---

## 5. Lessons Learned & Prevention

Optional follow-up actions:
- [ ] Evaluate if phishing training should be refreshed
- [ ] Add new IOCs or behaviors to alerting platform (NDR/SIEM)
- [ ] Adjust email or endpoint filtering if the attack vector was allowed through
