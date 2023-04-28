class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, start, end = len(s), 0, 0
        if n in [0, 1]:
            return s
        def palindromeLength(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l, r = l - 1, r + 1
            return r - l - 1
        for i in range(n):
            maxPalindromeLength = max(palindromeLength(i, i), palindromeLength(i, i + 1))
            if maxPalindromeLength > end - start:
                end, start = i + (maxPalindromeLength // 2), i - ((maxPalindromeLength - 1) // 2)
        return s[start : end + 1]