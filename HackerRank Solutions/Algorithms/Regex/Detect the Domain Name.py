import re

pattern = '(http|https)\\://(www.|ww2.|)([a-zA-Z0-9\\-\\.]+)(\\.[a-zA-Z]+)(/\\S*)?'
regex = re.compile(pattern)

s = set()

for i in range(int(input())):
    string = input()
    iterator = regex.finditer(string)
    if iterator:
        for match in iterator:
            s.add(match.group(3)+match.group(4))

print(';'.join(t for t in sorted(s)))
