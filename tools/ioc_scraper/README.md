# IOC Scraper + Aggregator

This tool extracts Indicators of Compromise (IOCs) from unstructured text files using regular expressions. It's designed for security professionals, analysts, and researchers who often deal with logs, threat intel dumps, or noisy report data.

## Usage

```bash
python ioc_scraper.py test_inputs/sample.txt
```
## What it Does

- Extracts IOCs from raw text:
  - IPv4 addresses
  - URLs
  - Domains
  - Email Addresses
  - SHA256 hashes
  - MD5 hashes
- Outputs results to:
    - Terminal (for quick review)
    - JSON and CSV files (for futher use)

