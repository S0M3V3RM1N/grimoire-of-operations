## Overview
Shodan is a search engine for internet-exposed services. You query its database of continuous scans; you’re not actively scanning targets. After shodan ran the 24 hour sale on a lifetime membership to shodan, I created a cheatsheet to reference how to get the most from this tool. 


### Core Query Syntax

- **Basic:** `keyword1 keyword2` (matches in banners/metadata)
    
- **Field filter:** `field:value` (quote values with spaces)
    
- **Boolean:** `AND` `OR` `NOT` (implicit AND between terms)
    
- **Ranges/Dates:** `before:YYYY-MM-DD` `after:YYYY-MM-DD`
    

### High‑Signal Filters (safe bets)

- **`port:`** — TCP/UDP port (e.g., `port:3389`)
    
- **`product:`** — Software name parsed from banners (e.g., `product:OpenSSH`)
    
- **`version:`** — Software version string (e.g., `product:nginx version:1.18.0`)
    
- **`org:`** — Organization/owner (WHOIS/GeoIP) (e.g., `org:"Janesville School District"`)
    
- **`asn:`** — Autonomous System Number (e.g., `asn:AS15169`)
    
- **`net:`** — CIDR/netblock (e.g., `net:203.0.113.0/24`)
    
- **`country:` / `city:`** — Geolocation (e.g., `country:US city:"Madison"`)
    
- **`hostname:`** — FQDN observed for the host (e.g., `hostname:*.example.org`)
    
- **`domain:`** — Root domain (e.g., `domain:example.org`)
    
- **`os:`** — OS parsed from banners (heuristic) (e.g., `os:Windows`)
    
- **`ssl.*`** — TLS fields (HTTP/HTTPS, SMTP STARTTLS, etc.)
    
    - `ssl.cert.subject.cn:"example.org"`
        
    - `ssl.cert.issuer.cn:"Let's Encrypt"`
        
    - `ssl.version:TLSv1.0` (useful for weak protocol hunting)
        
- **`http.title:`** — Page title extracted from HTTP (e.g., `http.title:"RouterOS"`)
    
- **`cpe:`** — Common Platform Enumeration (when parsed) (e.g., `cpe:cpe:/a:jenkins:jenkins`)
    
- **`tag:`** — Shodan tags (e.g., `tag:industrial-control-system`)
    
- **`vuln:`** — CVE identifier (availability depends on plan) (e.g., `vuln:CVE-2023-34362`)
    

> Tip: Combine filters narrowly: `port:9200 product:Elasticsearch country:US -ssl`.

---

### Ready‑to‑Use Query Patterns

### 1) Attack Surface Mapping (defensive recon)

- **Org exposure overview:** `org:"<Your Org Name>"`
    
- **Known netblocks:** `net:<CIDR>`; repeat for all allocations.
    
- **Web only (80/443):** `org:"<Your Org Name>" port:80 OR port:443`
    
- **New exposure last 7d:** `org:"<Your Org Name>" after:<YYYY-MM-DD>`
    
- **Certificate pivots:** `ssl.cert.subject.cn:"yourdomain.com" OR hostname:"*.yourdomain.com"`
    

### 2) Weak/Legacy Protocols

- **RDP exposed:** `port:3389`
    
- **SMB exposed:** `port:445` (pairs well with `os:Windows`)
    
- **Telnet:** `port:23`
    
- **FTP (plaintext):** `port:21`
    
- **Outdated TLS:** `ssl.version:TLSv1 OR ssl.version:SSLv3`
    

### 3) Common High‑Risk Services

- **Elasticsearch (no auth by default):** `port:9200 product:Elasticsearch`
    
- **MongoDB:** `port:27017 product:MongoDB`
    
- **Redis:** `port:6379 product:Redis`
    
- **Kibana:** `port:5601 http.title:Kibana`
    
- **Jenkins:** `http.title:Jenkins`
    
- **Grafana:** `http.title:Grafana`
    
- **vSphere/vCenter:** `product:"VMware ESXi" OR http.title:"VMware vSphere"`
    

### 4) IoT / Admin Panels

- **Printers:** `port:9100 OR product:JetDirect`
    
- **Cameras:** `product:"GoAhead-Webs" OR http.title:camera`
    
- **NAS/Web UIs:** `http.title:"Synology" OR http.title:"QNAP"`
    

### 5) Certificate/Domain Hygiene

- **Mismatched certs:** `ssl.cert.subject.cn:yourdomain.com -hostname:*.yourdomain.com`
    
- **Let’s Encrypt inventory:** `ssl.cert.issuer.cn:"Let's Encrypt" domain:yourdomain.com`
    

---

### SOC Workflows

### Exposure Review (Weekly)

1. Query `org:` + `net:` ranges; export results.
    
2. Filter to _new_ since last review using `after:`.
    
3. Prioritize by service risk (e.g., 3389/445/9200/27017).
    
4. Pivot by `ssl.cert.subject.cn` to detect shadow IT.
    

### Incident Triage

- **Indicator pivot:** Search IP/domain from alert in Shodan to see other open services, past banners, and certs.
    
- **Tech fingerprint:** Add `product:` `version:` to scope likely vuln exposure.
    
- **Count first:** `api.count(query)` (fast cardinality) → then page search for details.
    

---

### CLI Quickstart (nice for one‑offs)

```bash
# Install
pipx install shodan  # or: pip install shodan

# Configure once
shodan init <YOUR_API_KEY>

# Examples
shodan search 'org:"Acme Corp" port:443'
shodan count 'port:3389 country:US'
shodan host 203.0.113.25
shodan download acme443 'org:"Acme Corp" port:443'
shodan parse acme443.json.gz --fields ip_str,port,org,hostnames
```

---

### Python API Basics (Shodan official library)

```python
# pip install shodan
import os, shodan

API_KEY = os.getenv("SHODAN_API_KEY", "<YOUR_API_KEY>")
api = shodan.Shodan(API_KEY)

# 1) Fast cardinality check
q = 'org:"Acme Corp" port:3389'
print(api.count(q))  # {'total': <int>, 'facets': {...}}

# 2) Paged search (respect rate limits)
page = 1
while True:
    res = api.search(q, page=page)
    for m in res.get('matches', []):
        print(m['ip_str'], m.get('port'), m.get('hostnames'))
    if len(res.get('matches', [])) == 0:
        break
    page += 1

# 3) Host detail (banner history, vulns when available)
host = api.host('203.0.113.25')
print(host['ip_str'], host.get('org'))
for item in host.get('data', []):
    print(item.get('port'), item.get('product'), item.get('transport'))
```

**Notes**

- Use environment variable `SHODAN_API_KEY` for local dev and CI.
    
- `api.search()` supports `page` (1‑indexed). Use `api.count()` to estimate pages.
    
- Respect plan rate limits; add sleeps/retries as needed.
    

---

### Lightweight Netblock Monitor (Defender‑minded)

```python
"""
Goal: Alert when *new* services appear in your netblocks.
- Keep a local JSON state of (ip, port, product) tuples.
- On each run: query Shodan, diff against state, print new items.
"""
import os, json, time, shodan
API_KEY = os.getenv('SHODAN_API_KEY', '<KEY>')
BLOCKS = ['198.51.100.0/24', '203.0.113.0/24']
STATE_FILE = 'shodan_state.json'

api = shodan.Shodan(API_KEY)
state = json.load(open(STATE_FILE)) if os.path.exists(STATE_FILE) else {}

new_findings = []
for block in BLOCKS:
    q = f'net:{block}'
    page = 1
    while True:
        res = api.search(q, page=page)
        matches = res.get('matches', [])
        if not matches: break
        for m in matches:
            key = f"{m['ip_str']}:{m.get('port')}:{m.get('product','')}"
            if key not in state:
                new_findings.append({
                    'ip': m['ip_str'], 'port': m.get('port'),
                    'product': m.get('product'), 'timestamp': m.get('timestamp')
                })
                state[key] = 1
        page += 1

if new_findings:
    print('[+] New exposure found:')
    for n in new_findings:
        print(n)
    json.dump(state, open(STATE_FILE,'w'), indent=2)
else:
    print('[=] No changes')
```


[Breakdown_of_Shodan_Script](breakdown_of_Shodan_Script.md)

---

### Practical Tips & Gotchas

- **Data is near‑real‑time, not instant.** Cross‑check with `nmap` for live validation.
    
- **Banner parsing isn’t perfect.** If `product:` misses, fall back to `http.title:` or keywords.
    
- **Quote multi‑word values.** `org:"Acme Education Services"`.
    
- **Be precise before broad.** Start with `net:`/`org:` then widen.
    
- **Respect scope & law.** Use on your own assets or with explicit authorization; treat findings as incident reports, not trophies.
    

---

### Quick Reference Table

|Goal|Example Query|
|---|---|
|All public web in org|`org:"Acme Corp" (port:80 OR port:443)`|
|Find accidental RDP|`org:"Acme Corp" port:3389`|
|Shadow IT via certs|`ssl.cert.subject.cn:"acme.com" -hostname:*.acme.com`|
|Elasticsearch open|`product:Elasticsearch port:9200`|
|Mongo exposed|`product:MongoDB port:27017`|
|TLS1.0 endpoints|`ssl.version:TLSv1`|
|Count first|_(CLI)_ `shodan count 'org:"Acme" port:445'`|

---

### Integrating the API (Step‑by‑Step)

1. **Get your key:** From your Shodan account → _API Key_.
    
2. **Store securely:** `export SHODAN_API_KEY="<key>"` (macOS/Linux) or set in your password manager/CI secrets.
    
3. **Install tools:** `pip install shodan` (library + CLI).
    
4. **CLI init:** `shodan init $SHODAN_API_KEY` → quick searches & exports.
    
5. **Python integration:** Use the code examples above (search, count, host). Wrap in a scheduled job for weekly exposure reviews.
    
6. **Data handling:** Keep a local state or push results to your SIEM (CSV/JSON → Logstash/Fluentd). Consider hashing IPs if sharing screenshots publicly.
    

---

## Ethical Use

Operate within authorized scope. For third‑party exposures discovered unintentionally, follow coordinated disclosure norms via abuse contacts or CERT channels.
