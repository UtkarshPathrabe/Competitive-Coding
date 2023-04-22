class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        sReverse = s[::-1]
        @lru_cache(None)
        def lcs(n1: int, n2: int) -> int:
            if n1 == 0 or n2 == 0:
                return 0
            if s[n1 - 1] == sReverse[n2 - 1]:
                return 1 + lcs(n1 - 1, n2 - 1)
            return max(lcs(n1 - 1, n2), lcs(n1, n2 - 1))
        return n - lcs(n, n)