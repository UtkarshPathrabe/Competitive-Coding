class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        m = 0
        for c in s:
            if c == '0':
                m += 1
        result = m
        for c in s:
            if c == '0':
                m -= 1
                result = min(result, m)
            else:
                m += 1
        return result