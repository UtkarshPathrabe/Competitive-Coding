import re

pattern = '<\s*(\w+).*?/?>'
regex = re.compile(pattern)

tags = set()

for num in range(int(input())):
    string = input()
    match_tags = regex.findall(string)
    tags.update(match_tags)

print(';'.join(t for t in sorted(tags)))
