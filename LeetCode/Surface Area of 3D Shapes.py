class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        result, n = 0, len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    result += 2
                    for r, c in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                        if 0 <= r < n and 0 <= c < n:
                            val = grid[r][c]
                        else:
                            val = 0
                        result += max(grid[i][j] - val, 0)
        return result