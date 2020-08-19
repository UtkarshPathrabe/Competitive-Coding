class Solution:
    def longestPalindrome(self, s: str) -> str:
        strLength = len(s)
        if strLength == 0 or strLength == 1:
            return s
        startIndex, endIndex = 0, 0
        def isPalindrome(s, sLength, L, R):
            while L >= 0 and R < sLength and s[L] == s[R]:
                L -= 1
                R += 1
            return R - L - 1
        for i in range(strLength):
            len1 = isPalindrome(s, strLength, i, i)
            len2 = isPalindrome(s, strLength, i, i + 1)
            maxLength = max(len1, len2)
            if maxLength > endIndex - startIndex:
                startIndex = i - (maxLength - 1) // 2
                endIndex = i + maxLength // 2
        return s[startIndex: endIndex + 1]