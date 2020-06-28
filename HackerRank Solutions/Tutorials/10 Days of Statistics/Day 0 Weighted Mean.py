N = int(input())
X = list(map(int, input().strip().split()))
W = list(map(int, input().strip().split()))
weightedSum = 0
weightSum = 0

for i in range(0, N):
    weightedSum += (W[i] * X[i])
    weightSum += W[i]

print(round((weightedSum / weightSum), 1))