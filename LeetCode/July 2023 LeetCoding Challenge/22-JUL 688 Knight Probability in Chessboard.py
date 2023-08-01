class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        VALID_MOVES = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        for _ in range(K):
            dp2 = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in VALID_MOVES:
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r + dr][c + dc] += val / 8.0
            dp = dp2
        return sum(map(sum, dp))