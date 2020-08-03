MOD = 10**9 + 7
N = int(input())
rootArray = [i for i in range(N+1)]
rankArray = [0] * (N+1)
sizeArray = [1] * (N+1)

def findSet(v):
    if rootArray[v] != v:
        rootArray[v] = findSet(rootArray[v])
    return rootArray[v]

def setUnion(value1, value2):
    root1 = findSet(value1)
    root2 = findSet(value2)
    if root1 != root2:
        if rankArray[root1] < rankArray[root2]:
            sizeArray[root2] += sizeArray[root1]
            rootArray[root1] = root2
            rankArray[root2] += 1
        else:
            sizeArray[root1] += sizeArray[root2]
            rootArray[root2] = root1
            rankArray[root1] += 1

for _ in range(N - 1):
    X, Y, color = list(input().strip().split())
    if color == 'b':
        setUnion(int(X), int(Y))

setSizes = [sizeArray[i] for i in range(1, N+1) if rootArray[i] == i]

p1 = [0]
for x in setSizes:
    p1.append((p1[-1] + x) % MOD)

p2 = [0]
for i, x in enumerate(setSizes):
    p2.append((p2[-1] + (x * p1[i])) % MOD)

p3 = [0]
for i, x in enumerate(setSizes):
    p3.append((p3[-1] + (x * p2[i])) % MOD)

print(p3[-1])