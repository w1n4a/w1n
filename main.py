import os
import requests
import sys

args = sys.argv
path = r"https://raw.githubusercontent.com/w1n4a/w1n/refs/heads/main/.json"
json = requests.get(path).json()

if len(args) == 3 and args[1] == 'ins' and args[2] in json:
    os.system(json[args[2]])

elif len(args) == 1:
    print("""
        w1n — Cross-platform environment automation manager

        Usage:
          w1n ins <package_name>      Download and deploy package from the cloud matrix

        Examples:
          w1n ins crab
""")
