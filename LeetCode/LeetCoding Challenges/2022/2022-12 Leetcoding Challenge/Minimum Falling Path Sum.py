class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        for i in range(1, M):
            for j in range(N):
                a = A[i - 1][j - 1] if 0 <= j - 1 else float('inf')
                b = A[i - 1][j]
                c = A[i - 1][j + 1] if j + 1 < N else float('inf')
                A[i][j] += min(a, b, c)
        return min(A[M - 1])