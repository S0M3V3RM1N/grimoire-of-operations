# The IoC Scraper
# This script is a work in progress, further implementations planned. 

import sys
import os
from regex_patterns import extract_iocs
from io_handler import read_text_file, write_json, write_csv

def main(input_path):
    if not os.path.exists(input_path):
        print(f"[!] File not found: {input_path}")
        return

    raw_text = read_text_file(input_path)
    iocs = extract_iocs(raw_text)

    print("\n[+] Extracted IOCs:\n")
    for ioc_type, values in iocs.items():
        if values:
            print(f"  {ioc_type.upper()}:")
            for v in values:
                print(f"    - {v}")
        else:
            print(f"  {ioc_type.upper()}: None")

    # Save to files
    base = os.path.basename(input_path).split('.')[0]
    write_json(f"output/{base}_iocs.json", iocs)
    write_csv(f"output/{base}_iocs.csv", iocs)
    print(f"\n[+] Results saved to output/{base}_iocs.json and .csv")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ioc_scraper.py <input_file.txt>")
    else:
        main(sys.argv[1])
