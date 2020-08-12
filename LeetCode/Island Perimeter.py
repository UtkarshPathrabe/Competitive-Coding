class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        numberOfRows = len(grid)
        numberOfColumns = len(grid[0])
        perimeter = 0
        for row in range(numberOfRows):
            for column in range(numberOfColumns):
                if grid[row][column] == 1:
                    perimeter += 4
                    if row > 0 and grid[row - 1][column] == 1:
                        perimeter -= 2
                    if column > 0 and grid[row][column - 1] == 1:
                        perimeter -= 2
        return perimeter