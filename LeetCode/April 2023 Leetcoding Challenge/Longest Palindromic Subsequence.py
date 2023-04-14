class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def helper(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if s[l] == s[r]:
                return 2 + helper(l + 1, r - 1)
            else:
                return max(helper(l + 1, r), helper(l, r - 1))
        
        return helper(0, n - 1)