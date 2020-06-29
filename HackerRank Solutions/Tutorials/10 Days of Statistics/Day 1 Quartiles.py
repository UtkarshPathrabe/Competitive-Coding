n = int(input())
X = sorted(list(map(int, input().strip().split())))
from statistics import median
print(int(median(X[:n//2])))
print(int(median(X)))
print(int(median(X[(n+1)//2:])))