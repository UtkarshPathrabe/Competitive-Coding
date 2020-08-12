class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        LAND = 1
        WATER = 0
        maxArea = 0
        numberOfRows = len(grid)
        if numberOfRows == 0:
            return maxArea
        numberOfColumns = len(grid[0])
        
        def dfs(grid, row, column):
            if row < 0 or row >= numberOfRows or column < 0 or column >= numberOfColumns or grid[row][column] != LAND:
                return 0
            else:
                grid[row][column] = WATER
                a = dfs(grid, row - 1, column)
                b = dfs(grid, row + 1, column)
                c = dfs(grid, row, column - 1)
                d = dfs(grid, row, column + 1)
                return a + b + c + d + 1
        
        for row in range(numberOfRows):
            for column in range(numberOfColumns):
                if grid[row][column] == LAND:
                    area = dfs(grid, row, column)
                    maxArea = max(area, maxArea)
        return maxArea