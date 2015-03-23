import re
import sys

N = int(input())
pattern = '[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}'
regexp = re.compile(pattern)

for i in range(0, N):
    match = regexp.match(input())
    if match:
        print("VALID")
    else:
        print("INVALID")
