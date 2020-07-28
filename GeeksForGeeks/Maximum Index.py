T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().strip().split()))
    minFromLeft = [0] * N
    maxFromRight = [0] * N
    minFromLeft[0] = A[0]
    for i in range(1, N):
        minFromLeft[i] = min(A[i], minFromLeft[i-1])
    maxFromRight[N-1] = A[N-1]
    for i in range(N-2, -1, -1):
        maxFromRight[i] = max(A[i], maxFromRight[i+1])
    diff = 0
    i, j = 0, 0
    while i < N and j < N:
        if minFromLeft[i] <= maxFromRight[j]:
            diff = max(diff, j - i)
            j += 1
        else:
            i += 1
    print(diff)