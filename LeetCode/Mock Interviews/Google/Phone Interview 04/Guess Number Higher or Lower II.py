class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for length in range(2, n + 1):
            for start in range(1, n - length + 2):
                minResult = float('inf')
                for pivot in range(start + (length - 1) // 2, start + length - 1):
                    result = pivot + max(dp[start][pivot - 1], dp[pivot + 1][start + length - 1])
                    minResult = min(result, minResult)
                dp[start][start + length - 1] = minResult
        return dp[1][n]