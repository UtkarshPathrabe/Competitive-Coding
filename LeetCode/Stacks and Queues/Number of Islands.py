class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        LAND = '1'
        WATER = '0'
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        numberOfIslands = 0
        numberOfRows = len(grid)
        if numberOfRows == 0:
            return numberOfIslands
        numberOfColumns = len(grid[0])
        for row in range(numberOfRows):
            for column in range(numberOfColumns):
                if grid[row][column] == LAND:
                    numberOfIslands += 1
                    queue = deque()
                    grid[row][column] = WATER
                    queue.append((row, column))
                    while queue:
                        rowNumber, columnNumber = queue.popleft()
                        for rowDirection, columnDirection in DIRECTIONS:
                            r = rowNumber + rowDirection
                            c = columnNumber + columnDirection
                            if r < 0 or c < 0 or r >= numberOfRows or c >= numberOfColumns or grid[r][c] != LAND:
                                continue
                            grid[r][c] = WATER
                            queue.append((r, c))
        return numberOfIslands