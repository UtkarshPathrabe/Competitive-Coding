class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m+1)]
        counter = [[s.count('0'), s.count('1')] for s in strs]
        for zeros, ones in counter:
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i-zeros][j-ones])
        return dp[-1][-1]