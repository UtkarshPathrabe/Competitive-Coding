class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        dp = [[[False for j in range(n)] for i in range(n)] for l in range(n + 1)]
        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]
        for length in range(2, n + 1):
            for i in range(n + 1 - length):
                for j in range(n + 1 - length):
                    for newLength in range(1, length):
                        dp1 = dp[newLength][i]
                        dp2 = dp[length - newLength][i + newLength]
                        dp[length][i][j] |= dp1[j] and dp2[j + newLength]
                        dp[length][i][j] |= dp1[j + length - newLength] and dp2[j]
        return dp[n][0][0]