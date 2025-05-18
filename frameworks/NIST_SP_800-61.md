# Gold Standards in Information Security 

The National Institute of Standards and Technology (NIST) is a non-regulatory U.S. federal agency that produces frameworks and the standards within. This helps organizations stregethen their security posture and adhere to best practices.

NIST's 800 series is what we will be focusing on here as it is directly related to information security and blue team operations. 

NIST Special Publication (SP)
 - NIST SP 800-61 Rev. 2: *Computer Security Incident Handling Guide*

There is a lot of information out there when googling this information yourself. This subdirectory will serve to consolidate information for both practicing and aspiring cybersecurity professionals. Use this as a quick reference, refresher, or initial exposure. 

---

# NIST SP 800-61 Rev. 2 – The IR Blueprint

**800-61 Rev. 2** is *the* gold standard for setting up an Incident Response program. It defines the incident response lifecycle, broken down into four phases:

## 1. Preparation
 - Establish and train an IR team
 - Build playbooks and test them
 - Harden Systems and establish logging/monitoring
 - Define communication channels and escalation paths

## 2. Detection and Analysis 
 - Monitor for anomalies via logs, SIEMs, EDRs, IDS/IPS
 - Validate that an incident occurred
 - Categorize the incident (e.g., DoS, insider threat, malware)

***Important Concepts*** 
 - Indicators of compromise (IOCs)
 - Use triage logics to confirm incident scope and severity (see triage_tips.md)
 - Document and timestamp **everything**

## 3. Containment, Eradication, and Recovery  
 - Stop the bleeding (containment)
 - Remove root cause (eradication)
 - Restory systems and validate operational status (recovery)

***Best Practices***
 - Short-term vs long-term containment
 - Reimage or rebuild systems when needed
 - Patch and monitor restored systems carefully

## 4. Post-Incident Activity
 - Conduct lessons-learned meetings (within the first 2 weeks)
 - Update IR documentation and controls (or create them if an organization never had anything in place)
 - Feed findings into future risk assessments

***Artifacts to Create:***
 - Incident Summary Reports
 - Root cause analysis (RCA)
 - Metrics: time-to-detect, time-to-contain, etc.

