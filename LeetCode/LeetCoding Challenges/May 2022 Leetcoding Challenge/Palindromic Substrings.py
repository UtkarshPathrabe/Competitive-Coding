class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindromeAroundCenter(low, high):
            result = 0
            while low > -1 and high < len(s):
                if s[low] != s[high]:
                    break
                low, high, result = low - 1, high + 1, result + 1
            return result
        result = 0
        for i in range(len(s)):
            result += countPalindromeAroundCenter(i, i)
            result += countPalindromeAroundCenter(i, i + 1)
        return result