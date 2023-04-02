class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols, nonObstacles, startCell, pathCount = len(grid), len(grid[0]), 0, [0, 0], 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    startCell = [row, col]
                if grid[row][col] == 0 or grid[row][col] == 2:
                    nonObstacles += 1
        
        def backtrack(cell, remainNonObstacles):
            nonlocal pathCount
            if grid[cell[0]][cell[1]] == 2 and remainNonObstacles == 0:
                pathCount += 1
                return
            cellValue = grid[cell[0]][cell[1]]
            grid[cell[0]][cell[1]] = -2
            for newDirection in DIRECTIONS:
                newCell = [cell[0] + newDirection[0], cell[1] + newDirection[1]]
                if 0 <= newCell[0] < rows and 0 <= newCell[1] < cols and grid[newCell[0]][newCell[1]] >= 0:
                    backtrack(newCell, remainNonObstacles - 1)
            grid[cell[0]][cell[1]] = cellValue
        
        backtrack(startCell, nonObstacles)
        return pathCount