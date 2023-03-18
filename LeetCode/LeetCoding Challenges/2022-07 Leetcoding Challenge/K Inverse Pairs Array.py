class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp, M = [0] * (k + 1), 10**9 + 7
        for i in range(1, n + 1):
            temp = [0] * (k + 1)
            temp[0] = 1
            for j in range(1, k + 1):
                val = (dp[j] + M - (dp[j - i] if j - i >= 0 else 0)) % M
                temp[j] = (temp[j - 1] + val) % M
            dp = temp
        return (dp[k] + M - (dp[k - 1] if k > 0 else 0)) % M