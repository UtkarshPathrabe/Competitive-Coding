class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def isNice(s: str) -> bool:
            charSet = set(s)
            if len(charSet) % 2 == 1:
                return False
            for char in s:
                if char >= 'A' and char <= 'Z':
                    if chr(ord(char) + 32) not in charSet:
                        return False
                else:
                    if chr(ord(char) - 32) not in charSet:
                        return False
            return True
        result = ''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                subString = s[i: j]
                if isNice(subString) and len(subString) > len(result):
                    result = subString
        return result