# SOC 2 Compliance Operational Guide

This guide provides a structured overview of SOC 2 compliance, focusing on actionable insights, trust criteria, and control considerations. It is intended for cybersecurity professionals maintaining security and privacy practices aligned with industry expectations, and is part of the Grimoire of Operations.

---

## 1. What is SOC 2?

**SOC 2 (System and Organization Controls 2)** is an auditing standard developed by the American Institute of Certified Public Accountants (AICPA) that evaluates how service organizations handle data in relation to the **Trust Services Criteria (TSC)**:

* Security (required)
* Availability
* Processing Integrity
* Confidentiality
* Privacy

SOC 2 reports are conducted by independent auditors and are specific to each organization’s controls and practices.

---

## 2. Report Types

### Type I

* Snapshot of controls at a specific point in time.
* Evaluates *design* of controls only.

### Type II

* Observation over a period (typically 3-12 months).
* Evaluates *design* and *operational effectiveness*.

---

## 3. Trust Services Criteria (TSC)

Each criterion contains specific control objectives. All SOC 2 reports must address **Security**; the others are optional based on the organization’s services.

### 3.1 Security (Common Criteria)

* Logical access controls
* System operations monitoring
* Change management
* Risk assessments

### 3.2 Availability

* Backup and disaster recovery
* System uptime and performance monitoring
* Incident handling for service disruption

### 3.3 Processing Integrity

* Data accuracy and completeness
* Input validation and processing logs
* Monitoring for processing errors

### 3.4 Confidentiality

* Data classification
* Encryption in transit and at rest
* Access based on least privilege

### 3.5 Privacy

* Data collection, use, and retention policies
* Consent management
* Individual data rights (access, deletion, correction)

---

## 4. Key Compliance Requirements

### 4.1 Policies and Procedures

* Must be clearly defined, documented, communicated, and enforced.
* Includes access control, incident response, change management, and vendor risk policies.

### 4.2 Security Controls

* MFA for internal and external access
* Logging and monitoring (SIEM integration recommended)
* Vulnerability management

### 4.3 Risk Management

* Periodic risk assessments
* Third-party/vendor risk evaluation
* Remediation tracking

### 4.4 Evidence Collection

* Control execution proof (logs, screenshots, reports)
* Audit trails for incidents, user provisioning, and configuration changes

### 4.5 Personnel and Training

* Background checks
* Role-based security awareness training
* Acknowledgment of policies

---

## 5. Audit Preparation

### Readiness Assessment (Gap Analysis)

* Map existing controls to relevant Trust Services Criteria
* Identify deficiencies or missing controls

### Remediation Phase

* Implement necessary controls and processes
* Establish documentation for repeatability

### Observation Period (for Type II)

* Maintain consistent execution
* Collect evidence as controls are exercised

### Final Audit

* Conducted by a CPA firm
* SOC 2 report issued based on findings

---

## 6. Continuous Compliance Tips

* Automate evidence collection using GRC or audit platforms (e.g., Drata, Vanta, Tugboat Logic)
* Integrate compliance tasks into existing workflows (JIRA, Slack, GitHub)
* Schedule quarterly internal reviews
* Maintain version-controlled policy documents

---

## 7. Reputable Sources

* AICPA Trust Services Criteria: [https://www.aicpa.org/interestareas/frc/assuranceadvisoryservices/trustservicescriteria.html](https://www.aicpa.org/interestareas/frc/assuranceadvisoryservices/trustservicescriteria.html)
* AICPA SOC Reports Overview: [https://www.aicpa.org/soc](https://www.aicpa.org/soc)
* Cloud Security Alliance (CSA) STAR program
* Center for Internet Security (CIS) Controls (mapped by some orgs for SOC 2 alignment)

---

## 8. Alignment with Other Frameworks

| SOC 2           | Comparable Frameworks              |
| --------------- | ---------------------------------- |
| Security        | NIST CSF, ISO/IEC 27001            |
| Availability    | ISO 22301, ITIL                    |
| Confidentiality | HIPAA, ISO/IEC 27701               |
| Privacy         | GDPR, CCPA, NIST Privacy Framework |

SOC 2 is **not** prescriptive. Organizations design their own controls as long as they meet the intent of the applicable Trust Services Criteria.

---

**Note:** SOC 2 compliance is not a one-time task but a continuous discipline. Operational maturity, consistent documentation, and cultural adoption are critical for success.
