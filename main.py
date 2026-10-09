import os
import requests
import sys

args = sys.argv
path = r"https://raw.githubusercontent.com/w1n4a/w1n/refs/heads/main/.json"
json = requests.get(path).json()

if args[1] == '-S' and len(args) == 3 and args[2] in json:
    os.system(json[args[2]])
    print(f"Downoload {args[1]}")
