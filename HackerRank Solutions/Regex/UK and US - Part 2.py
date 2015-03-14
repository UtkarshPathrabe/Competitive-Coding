import re

text = " "
for i in range(0, int(input())):
    text = text + input() + " "

revised = re.sub('or', 'our', text)
for i in range(0, int(input())):
    print(revised.count(input() + " "))
