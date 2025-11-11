# MITRE ATT&CK Framework Overview

The **MITRE ATT&CK® Framework** is a continuously updated knowledge base of real-world adversary behaviors. It focuses not on theoretical models or specific technologies, but on how attackers actually operate from **initial access** to **data exfiltration**.

ATT&CK shifts cybersecurity from reactive defense to behavioral understanding. It provides a common language and structured way to analyze and defend against adversaries. The MITRE ATT&CK website is a critical part in understanding the tactics and techniques used in the wild. Additionally, APT tracking is another part of the website that can be used for threat intelligence/research. Tactics and techniques are mapped to the APT groups showcasing what a group is/was actively using in their attacks. 

---

## Why It Matters

* Establishes a **shared taxonomy** for describing attacks across teams and organizations.
* Maps **red team and threat actor behavior** to known adversary techniques.
* Drives **detection engineering**, **threat hunting**, and **incident response** strategies.
* Focuses defenders on **tactics, techniques, and procedures (TTPs)** — persistent behavioral patterns that remain even as tooling changes.

---

## Core Concepts

| Concept            | Description                                                                           | Example                              |
| ------------------ | ------------------------------------------------------------------------------------- | ------------------------------------ |
| **Tactics**        | The *objectives* of the attacker — the “why.”                                         | Persistence, Defense Evasion         |
| **Techniques**     | The *methods* used to achieve those objectives — the “how.”                           | Registry Run Keys, Obfuscated Files  |
| **Sub-Techniques** | More detailed, specific implementations of a technique.                               | `T1059.001` – PowerShell             |
| **Procedures**     | Real-world examples of techniques in use, often attributed to specific threat actors. | APT29 using credential dumping tools |

---

## Framework Structure

The ATT&CK Matrix organizes adversary behavior into stages reflecting the progression of an attack. Each column represents a **tactic**, and each cell a **technique**.

* **Enterprise ATT&CK** – For Windows, macOS, Linux, and cloud environments.
* **Mobile ATT&CK** – Covers Android and iOS ecosystems.
* **ICS ATT&CK** – For industrial control systems and OT environments.

Each domain is continuously updated based on community input and public threat intelligence.

---

## Application in Blue Team Operations

* **Detection Engineering:** Develop analytic rules mapped to ATT&CK techniques.
* **Threat Hunting:** Identify gaps and unusual patterns in telemetry aligned to ATT&CK TTPs.
* **Incident Response:** Classify activity according to ATT&CK mappings to understand adversary goals and progression.
* **Purple Teaming:** Coordinate red and blue team exercises using ATT&CK as a shared model.
* **Reporting and Metrics:** Measure defensive coverage by mapping detections and incidents to ATT&CK techniques.

---

## What This File Is

This markdown serves as a **high-level primer** on ATT&CK — designed for operators, defenders, and learners looking to ground themselves before exploring detailed implementations.

Additional documentation within this repository expands on specific areas(future creation planned):

* `tactics.md` – Walkthrough of each tactic with context and examples.
* `techniques/` – Individual markdowns breaking down key techniques.
* `use-cases.md` – Practical applications of ATT&CK in investigations and exercises.
* `mappings/` – Crosswalks between internal telemetry and ATT&CK coverage.

---

## External Resources

* [MITRE ATT&CK Website](https://attack.mitre.org/)
* [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)
* [MITRE ATT&CK GitHub Repository](https://github.com/mitre-attack/attack-navigator)
* [Red Canary ATT&CK Reports](https://redcanary.com/threat-detection-report/)
