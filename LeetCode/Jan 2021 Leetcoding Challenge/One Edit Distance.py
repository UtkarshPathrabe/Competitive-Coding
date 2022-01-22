class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        sLen, tLen = len(s), len(t)
        if sLen > tLen:
            return self.isOneEditDistance(t, s)
        if tLen - sLen > 1:
            return False
        for i in range(sLen):
            if s[i] != t[i]:
                if sLen == tLen:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]
        return sLen + 1 == tLen