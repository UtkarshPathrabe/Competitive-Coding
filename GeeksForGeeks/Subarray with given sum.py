T = int(input())
for _ in range(T):
    N, S = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))
    start, end = 0, 0
    currentSum = A[start]
    foundSum = False
    while end < N and start < N:
        if currentSum == S:
            foundSum = True
            break
        elif currentSum < S:
            end += 1
            if (end < N):
                currentSum += A[end]
        elif currentSum > S:
            if (start < N):
                currentSum -= A[start]
            start += 1
    if foundSum:
        print(start+1, end+1)
    else:
        print(-1)