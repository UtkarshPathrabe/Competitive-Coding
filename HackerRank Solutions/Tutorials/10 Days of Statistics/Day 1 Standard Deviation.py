import math
N = int(input())
X = list(map(int, input().strip().split()))
mean = sum(X) / N
diffSum = 0
for i in X:
    diffSum += (i - mean) ** 2
print(math.sqrt(diffSum / N))