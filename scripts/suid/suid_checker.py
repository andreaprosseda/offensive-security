import os
import requests

wordlist = 'suid_common.txt'
target_binaries = ''
safe_binaries = ''
vulnerable_binaries_url = 'https://gtfobins.github.io/#+suid'
#https://raw.githubusercontent.com/GTFOBins/GTFOBins.github.io/master/_gtfobins/python.md

def openFile(file_path):
    lines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = clean(lines)
    print(lines)

def clean(lines):
    result = []
    for line in lines:
        current = line.strip()
        if current:
            result.append(current)
    return result

openFile(target_binaries)
r = requests.get(url = vulnerable_binaries_url)
print(r)