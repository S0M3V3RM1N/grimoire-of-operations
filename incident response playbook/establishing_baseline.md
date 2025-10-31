# Log Correlation and Baselining Network Traffic

## Purpose

This document provides a structured approach to establishing and maintaining a baseline of normal network and system activity. A clear baseline enables effective anomaly detection, reduces alert fatigue, and supports threat hunting by distinguishing expected behavior from suspicious deviations.

## Objectives

* Define what "normal" looks like across critical infrastructure components.
* Identify and document regular patterns in logs, traffic, and user behavior.
* Create reference metrics and visualization methods for ongoing comparison.
* Support detection of policy violations, intrusions, or misconfigurations through deviation analysis.

## Data Sources

Focus on logs and telemetry that best represent operational activity:

| Category           | Example Sources                                    | Notes                                                          |
| ------------------ | -------------------------------------------------- | -------------------------------------------------------------- |
| **Network**        | Firewall, Switch Syslogs, NetFlow/SFlow            | Identify common destinations, ports, and protocols.            |
| **Authentication** | Google Workspace logs, AD Sign-Ins, SSO Providers  | Track login frequency, locations, and failure rates.           |
| **Endpoint**       | EDR Alerts, OS Event Logs, Sysmon                  | Establish normal process trees, scheduled tasks, and binaries. |
| **Email / Web**    | Secure Email Gateway, Proxy, DNS Resolver          | Monitor outbound connections and common domains.               |
| **Cloud**          | SaaS Admin Logs, API Calls, IAM Activity           | Observe normal user and service account behavior.              |

## Methodology

1. **Collect and Normalize Logs**

   * Ensure logs are centralized in a SIEM or log aggregator (e.g., Greylog, Wazuh, Splunk).
   * Standardize time synchronization and field naming across sources.

2. **Establish Observation Period**

   * Gather at least 30 days of continuous log data to capture business cycles.
   * Note recurring maintenance, patch windows, or scheduled backups.

3. **Quantify Normal Patterns**

   * Identify top talkers, frequent IPs, top ports, and login peaks.
   * Use visualization (e.g., heatmaps or histograms) to detect outliers.
   * Record metrics such as: average daily connections per host, authentication success/failure ratios, and DNS query volume.

4. **Document and Validate Baseline**

   * Record metrics in a version-controlled repository (like `/baselines/`).
   * Validate with system owners or administrators.
   * Include known exceptions and business-critical flows (e.g., backup traffic, content filters, update servers).

5. **Apply to Monitoring and Threat Hunting**

   * Compare new alerts or activity against baseline references.
   * Flag deviations beyond established thresholds for investigation.
   * Use the baseline to tune SIEM correlation rules, reducing false positives.

6. **Review and Update Regularly**

   * Reassess every quarter or after major infrastructure changes.
   * Automate data collection where possible to ensure consistency.

## Baseline Metrics Example

| Metric                                | Normal Range                    | Deviation Threshold       | Notes                                                              |
| ------------------------------------- | ------------------------------- | ------------------------- | ------------------------------------------------------------------ |
| Daily Outbound Connections (per host) | 300–500                         | >800                      | Sudden spikes may indicate malware beaconing or data exfiltration. |
| Failed Logins (per user, daily)       | 0–5                             | >10                       | May indicate brute-force attempts or forgotten credentials.        |
| DNS Queries (per client)              | 2000–5000                       | >7500                     | Useful to spot DNS tunneling or misconfigured clients.             |
| External Destinations                 | Known CDN, SaaS, Update Servers | Unknown IPs or rare ports | Can expose command-and-control channels.                           |

## Output and Reporting

* Store visual summaries and metrics in a secure dashboard or markdown logbook.
* Include timestamped reports showing baseline trend changes.
* Annotate anomalies that were investigated but proven benign.

## Lessons Learned

* A baseline is never static—it evolves with network growth and policy changes.
* Documenting why deviations occur (e.g., new service rollout) prevents redundant investigations.
* Continuous review builds intuition for your environment, reducing time-to-detect during true incidents.
