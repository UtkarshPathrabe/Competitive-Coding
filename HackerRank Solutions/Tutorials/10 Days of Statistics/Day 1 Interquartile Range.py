n = int(input())
X = list(map(int, input().strip().split()))
F = list(map(int, input().strip().split()))
S = []
for i in range(0, n):
    S += [X[i]] * F[i]
S.sort()
N = len(S)
from statistics import median
q1 = int(median(S[:N//2]))
q3 = int(median(S[(N+1)//2:]))
print(round(float(q3 - q1), 1))