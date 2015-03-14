import re
import sys

patternIPv6 = '^([0-9a-f]{1,4}:){7}[0-9a-f]{1,4}$'
regexpIPv6 = re.compile(patternIPv6)
patternIPv4 = '^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])$'
regexpIPv4 = re.compile(patternIPv4)

for i in range(0, int(input())):
    string = input()
    matchIPv6 = regexpIPv6.match(string)
    matchIPv4 = regexpIPv4.match(string)
    if matchIPv6:
        print("IPv6")
    elif matchIPv4:
        print("IPv4")
    else:
        print("Neither")
