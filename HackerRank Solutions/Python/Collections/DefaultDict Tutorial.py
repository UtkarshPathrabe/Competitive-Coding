from collections import defaultdict
hashMap = defaultdict(list)
n, m = map(int, input().split())
for i in range(n):
    a = input()
    hashMap[a].append(str(i + 1))
for i in range(m):
    a = input()
    if a in hashMap:
        print(' '.join(hashMap[a]))
    else:
        print('-1')