# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
S = input()
freqMap = Counter(S)
l = []
for key, val in freqMap.items():
    l.append((-val, key))
l.sort()
for i in range(3):
    print(l[i][1], -l[i][0])