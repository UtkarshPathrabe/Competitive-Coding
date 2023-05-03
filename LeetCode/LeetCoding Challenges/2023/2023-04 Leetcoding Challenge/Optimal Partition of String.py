class Solution:
    def partitionString(self, s: str) -> int:
        charSet, substringCount = set(), 1
        for char in s:
            if char in charSet:
                charSet = set()
                substringCount += 1
            charSet.add(char)
        return substringCount