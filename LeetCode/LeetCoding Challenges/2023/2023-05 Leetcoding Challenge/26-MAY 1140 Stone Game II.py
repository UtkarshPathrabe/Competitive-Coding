class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @lru_cache(None)
        def helper(p: int, i: int, m: int) -> int:
            if i == n:
                return 0
            result, s = 10**6 if p == 1 else -1, 0
            for x in range(1, min(2 * m, n - i) + 1):
                s += piles[i + x - 1]
                if p == 0:
                    result = max(result, s + helper(1, i + x, max(x, m)))
                else:
                    result = min(result, helper(0, i + x, max(x, m)))
            return result
        return helper(0, 0, 1)