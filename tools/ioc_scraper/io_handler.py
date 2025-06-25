# io_handler reads the input file and outputs JSON and CSV files

import os
import json
import csv

def read_text_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def write_json(output_path, data):
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)

def write_csv(output_path, data):
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["IOC Type", "Value"])
        for ioc_type, values in data.items():
            for value in values:
                writer.writerow([ioc_type, value])
