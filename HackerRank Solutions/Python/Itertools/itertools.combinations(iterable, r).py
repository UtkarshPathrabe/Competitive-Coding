# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
S, k = input().split()
S = sorted(S)
k = int(k)
for i in range(1, k + 1):
    for c in list(combinations(S, i)):
        print(''.join(c))