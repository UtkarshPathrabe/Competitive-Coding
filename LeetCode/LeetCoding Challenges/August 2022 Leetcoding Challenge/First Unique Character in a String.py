class Solution:
    def firstUniqChar(self, s: str) -> int:
        charMap = Counter(s)
        for i, c in enumerate(s):
            if charMap[c] == 1:
                return i
        return -1