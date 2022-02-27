class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(maxsize=None)
        def dfs(remain):
            if remain == 0:
                return False
            sqrtRoot = int(remain ** 0.5)
            for i in range(sqrtRoot, 0, -1):
                if not dfs(remain - i * i):
                    return True
            return False
        return dfs(n)