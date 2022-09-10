class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if not prices or k == 0:
            return 0
        if 2*k >= n:
            result = 0
            for i, j in zip(prices[1:], prices[:-1]):
                result += max(0, i - j)
            return result
        dp = [[[0, -prices[0]] for _ in range(n)] for _ in range(k + 1)]
        result = 0
        for i in range(1, k + 1):
            for j in range(1, n):
                dp[i][j][0] = max(dp[i][j - 1][0], dp[i][j - 1][1] + prices[j])
                dp[i][j][1] = max(dp[i][j - 1][1], dp[i - 1][j - 1][0] - prices[j])
                if j == n - 1:
                    result = max(result, dp[i][j][0])
        return result