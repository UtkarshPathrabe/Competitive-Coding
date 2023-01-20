class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp, prefixSum = [[0] * n for _ in range(n)], [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + stones[i]
        for length in range(2, n + 1):
            for start in range(n + 1 - length):
                end = start + length - 1
                scoreRemoveFirst, scoreRemoveLast = prefixSum[end + 1] - prefixSum[start + 1], prefixSum[end] - prefixSum[start]
                dp[start][end] = max(scoreRemoveFirst - dp[start + 1][end], scoreRemoveLast - dp[start][end - 1])
        return dp[0][n - 1]