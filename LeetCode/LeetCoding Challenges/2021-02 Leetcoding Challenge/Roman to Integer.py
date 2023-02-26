class Solution:
    def romanToInt(self, s: str) -> int:
        charMap, i, result = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}, len(s) - 1, 0
        while i >= 0:
            if i > 0 and charMap[s[i]] > charMap[s[i - 1]]:
                result += (charMap[s[i]] - charMap[s[i - 1]])
                i -= 2
            else:
                result += charMap[s[i]]
                i -= 1
        return result