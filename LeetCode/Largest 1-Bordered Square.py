class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows, cols, result = len(grid), len(grid[0]), 0
        verMax, horMax = [[0] * cols for _ in range(rows)], [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                verMax[i][j] = grid[i][j] if i == 0 or grid[i][j] == 0 else verMax[i-1][j]+1
                horMax[i][j] = grid[i][j] if j == 0 or grid[i][j] == 0 else horMax[i][j-1]+1
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i + 1 <= result or j + 1 <= result:
                    break
                maxSize = min(verMax[i][j], horMax[i][j])
                for k in range(maxSize, -1, -1):
                    if k <= result:
                        break
                    if verMax[i][j - (k - 1)] >= k and horMax[i - (k - 1)][j] >= k:
                        result = max(result, k)
                        break
        return result * result