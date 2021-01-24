class Solution:
    def maxScore(self, s: str) -> int:
        dp = [0] * len(s)
        dp[-1] = 1 if s[-1] == '1' else 0
        for i in range(len(s) - 2, -1, -1):
            dp[i] = dp[i + 1] + (1 if s[i] == '1' else 0)
        result, numberOfZeroes = 0, 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                numberOfZeroes += 1
            result = max(result, numberOfZeroes + dp[i + 1])
        return result