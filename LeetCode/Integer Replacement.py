class Solution:
    def integerReplacement(self, n: int) -> int:
        @lru_cache
        def helper(num):
            if num <= 1:
                return 0
            if num % 2 == 0:
                return 1 + helper(num // 2)
            else:
                return 1 + min(helper(num - 1), helper(num + 1))
        return helper(n)