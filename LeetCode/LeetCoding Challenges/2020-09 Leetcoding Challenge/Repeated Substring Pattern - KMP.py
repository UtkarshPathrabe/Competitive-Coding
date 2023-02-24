class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            j = dp[i - 1]
            while j > 0 and s[i] != s[j]:
                j = dp[j - 1]
            if s[i] == s[j]:
                j += 1
            dp[i] = j
        l = dp[n - 1]
        return l != 0 and n % (n - l) == 0