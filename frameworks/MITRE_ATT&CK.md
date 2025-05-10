# MITRE ATT&CK Framework

The MITRE ATT&CK® Framework is a living matrix of known adversary behavior — not based on theory, but on real-world attacks. It doesn't care how advanced your firewall is or what brand name is on your EDR. ATT&CK tells you **how** attackers operate, step by step, from initial access to data exfiltration.

Where traditional models focus on the tools, ATT&CK emphasizes **tactics** (the "why") and **techniques** (the "how"). It’s not just about stopping malware — it’s about understanding the behavior behind it.

## Why It Matters

- It gives defenders a shared language to describe attacks.
- It maps red team activity to known threat behaviors.
- It fuels detection engineering, threat hunting, and incident response.
- It shifts focus from IOCs to TTPs — the behavior patterns that persist beyond tooling.

## Core Concepts

- **Tactics:** The goals of an attacker during an operation (e.g., Persistence, Defense Evasion).
- **Techniques:** The methods used to achieve those goals (e.g., Registry Run Keys, Obfuscated Files).
- **Sub-techniques:** More granular variations of a technique.
- **Procedures:** Specific real-world examples, often linked to threat actor groups.

## What This File Is

This markdown is a high-level primer — a launching point into ATT&CK. It’s not exhaustive, and it’s not formal. This is for operators, defenders, and learners who want to orient themselves before diving deeper.

Additional pages will expand on:

- `tactics.md` – A walkthrough of each tactic with examples.
- `techniques/` – Individual files breaking down specific techniques.
- `use-cases.md` – How we’ve applied ATT&CK in the real world.
- `mappings/` – How alerts, logs, and tools map to ATT&CK.

## External Resources

- [MITRE ATT&CK Site](https://attack.mitre.org/)
- [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)
- [Red Canary ATT&CK Reports](https://redcanary.com/threat-detection-report/)
- [MITRE ATT&CK GitHub](https://github.com/mitre-attack/attack)

---

*“You don’t stop a threat by reacting to the payload. You stop it by recognizing the pattern.”*
