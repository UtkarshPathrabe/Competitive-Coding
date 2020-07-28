T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().strip().split()))
    XOR = A[0]
    for i in range(1, N*2 + 2):
        XOR = XOR ^ A[i]
    rightmostSetBit = XOR & ~(XOR-1)
    X, Y = 0, 0
    for i in range(2*N + 2):
        if (A[i] & rightmostSetBit):
            X = X ^ A[i]
        else:
            Y = Y ^ A[i]
    print(min(X, Y), max(X, Y))