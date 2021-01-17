class Solution:
    def countVowelStrings(self, n: int) -> int:
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24
        # dp = [[0] * 6 for i in range(n + 1)]
        # for vowel in range(1, 6):
        #     dp[1][vowel] = vowel
        # for nValue in range(2, n + 1):
        #     dp[nValue][1] = 1
        #     for vowel in range(2, 6):
        #         dp[nValue][vowel] = dp[nValue - 1][vowel] + dp[nValue][vowel - 1]
        # return dp[n][5]