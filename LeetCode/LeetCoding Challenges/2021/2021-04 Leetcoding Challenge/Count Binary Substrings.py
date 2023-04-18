class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        currentCount, prevCount, result = 1, 0, 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                currentCount += 1
            else:
                result += min(currentCount, prevCount)
                prevCount = currentCount
                currentCount = 1
        return result + min(currentCount, prevCount)