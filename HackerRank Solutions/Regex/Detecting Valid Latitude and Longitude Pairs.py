import re
import sys

N = int(input())
pattern = '\([-+]?([1-9]\d*\.[0-9]+|[1-9]\d*),\s[-+]?([1-9]\d*\.[0-9]+|[1-9]\d*)\)'
regexp = re.compile(pattern)

for i in range(0, N):
    match = regexp.search(input())
    if match:
        lat = float(match.group(1))
        lon = float(match.group(2))
        if lat >= 0.0 and lat <= 90.0 and lon >= 0.0 and lon <= 180.0:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
