class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p, length = len(s) - 1, 0
        while p >= 0:
            if s[p] != ' ':
                length += 1
            else:
                if length > 0:
                    return length
            p -= 1
        return length