class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        LAND = '1'
        WATER = '0'
        numberOfIslands = 0
        numberOfRows = len(grid)
        if numberOfRows == 0:
            return numberOfIslands
        numberOfColumns = len(grid[0])
        
        def dfs(grid, row, column):
            if row >= numberOfRows or row < 0 or column >= numberOfColumns or column < 0 or grid[row][column] != LAND:
                return
            grid[row][column] = WATER
            dfs(grid, row - 1, column)
            dfs(grid, row + 1, column)
            dfs(grid, row, column - 1)
            dfs(grid, row, column + 1)
        
        for row in range(numberOfRows):
            for column in range(numberOfColumns):
                if grid[row][column] == LAND:
                    numberOfIslands += 1
                    dfs(grid, row, column)
        return numberOfIslands