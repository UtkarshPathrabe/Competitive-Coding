class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        M, memo = 10**9 + 7, [[[-1] * (maxMove + 1) for _ in range(n)] for _ in range(m)]
        def helper(remainingMoves, x, y):
            if x == m or y == n or x < 0 or y < 0:
                return 1
            if remainingMoves == 0:
                return 0
            if memo[x][y][remainingMoves] >= 0:
                return memo[x][y][remainingMoves]
            memo[x][y][remainingMoves] = (helper(remainingMoves - 1, x - 1, y) + helper(remainingMoves - 1, x, y - 1) + helper(remainingMoves - 1, x + 1, y) + helper(remainingMoves - 1, x, y + 1)) % M
            return memo[x][y][remainingMoves]
        return helper(maxMove, startRow, startColumn)