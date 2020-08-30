class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        numberOfRows = len(grid)
        numberOfColumns = len(grid[0])
        for row in range(numberOfRows):
            for col in range(numberOfColumns):
                if row == 0 and col == 0:
                    continue
                elif row == 0 and col != 0:
                    grid[row][col] += grid[row][col - 1]
                elif row != 0 and col == 0:
                    grid[row][col] += grid[row - 1][col]
                else:
                    grid[row][col] += min(grid[row][col - 1], grid[row - 1][col])
        return grid[numberOfRows - 1][numberOfColumns - 1]