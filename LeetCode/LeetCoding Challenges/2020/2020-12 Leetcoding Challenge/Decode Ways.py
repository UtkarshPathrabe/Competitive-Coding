class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        dp = [0 for _ in range(3)]
        dp[0] = 1
        dp[1] = int(s[0] != '0')
        for i in range(2, len(s) + 1):
            dp[i % 3] = 0
            if s[i - 1] != '0':
                dp[i % 3] += dp[(i - 1) % 3]
            twoDigitsNumber = int(s[i - 2: i])
            if twoDigitsNumber >= 10 and twoDigitsNumber <= 26:
                dp[i % 3] += dp[(i - 2) % 3]
        return dp[len(s) % 3]