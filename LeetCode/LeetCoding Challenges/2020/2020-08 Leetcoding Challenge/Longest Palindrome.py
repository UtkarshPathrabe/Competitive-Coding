class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        for value in Counter(s).values():
            result += (value // 2) * 2
            if result % 2 == 0 and value % 2 == 1:
                result += 1
        return result