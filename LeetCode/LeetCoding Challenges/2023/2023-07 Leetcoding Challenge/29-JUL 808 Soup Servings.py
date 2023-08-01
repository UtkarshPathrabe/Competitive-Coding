class Solution:
    def soupServings(self, n: int) -> float:
        m = math.ceil(n / 25)
        @lru_cache(None)
        def helper(i: int, j: int) -> float:
            if i <= 0 and j <= 0:
                return 0.5
            if i <= 0:
                return 1.0
            if j <= 0:
                return 0.0
            return (helper(i - 4, j) + helper(i - 3, j - 1) + helper(i - 2, j - 2) + helper(i - 1, j - 3)) / 4.0
        for k in range(1, m + 1):
            if helper(k, k) > 1 - 1e-5:
                return 1.0
        return helper(m, m)