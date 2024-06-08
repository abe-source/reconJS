#!/usr/bin/env python3
import re
import sys

def extract_strings_from_js(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Regex to match strings within quotes but not single character variables
    strings = re.findall(r'(?<!\w)("([^"]{2,})"|\047([^\'\x7f-\xff]{2,})\047)', content)
    
    # Extract the strings without the surrounding quotes
    result = [match[1] if match[1] else match[2] for match in strings]
    
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_js_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    extracted_strings = extract_strings_from_js(file_path)
    for item in extracted_strings:
        print(item)
