# regex patterns to match common IoCs 

import re

PATTERNS = {
    "ipv4": r"\b(?:(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\b",
    "email": r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b",
    "url": r"\bhttps?://[^\s/$.?#].[^\s]*\b",
    "domain": r"\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
    "sha256": r"\b[A-Fa-f0-9]{64}\b",
    "md5": r"\b[a-fA-F0-9]{32}\b"
}

def extract_iocs(text):
    results = {}
    for ioc_type, pattern in PATTERNS.items():
        matches = re.findall(pattern, text)
        results[ioc_type] = sorted(set(matches))
    return results
