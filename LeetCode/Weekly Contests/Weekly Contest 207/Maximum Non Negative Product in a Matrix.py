class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        rows, cols = len(grid), len(grid[0])
        productDP = [[[float('-inf'), float('inf')] for _ in range(cols)] for _ in range(rows)]
        productDP[0][0] = [max(productDP[0][0][0], grid[0][0]), min(productDP[0][0][1], grid[0][0])]
        for row in range(1, rows):
            tempMax = max(grid[row][0] * productDP[row - 1][0][0], grid[row][0] * productDP[row - 1][0][1], productDP[row][0][0])
            tempMin = min(grid[row][0] * productDP[row - 1][0][0], grid[row][0] * productDP[row - 1][0][1], productDP[row][0][1])
            productDP[row][0] = [tempMax, tempMin]
        for col in range(1, cols):
            tempMax = max(grid[0][col] * productDP[0][col - 1][0], grid[0][col] * productDP[0][col - 1][1], productDP[0][col][0])
            tempMin = min(grid[0][col] * productDP[0][col - 1][0], grid[0][col] * productDP[0][col - 1][1], productDP[0][col][1])
            productDP[0][col] = [tempMax, tempMin]
        for row in range(1, rows):
            for col in range(1, cols):
                tempMax = max(grid[row][col] * productDP[row - 1][col][0], grid[row][col] * productDP[row - 1][col][1], productDP[row][col][0], grid[row][col] * productDP[row][col - 1][0], grid[row][col] * productDP[row][col - 1][1])
                tempMin = min(grid[row][col] * productDP[row - 1][col][0], grid[row][col] * productDP[row - 1][col][1], productDP[row][col][1], grid[row][col] * productDP[row][col - 1][0], grid[row][col] * productDP[row][col - 1][1])
                productDP[row][col] = [tempMax, tempMin]
        result = max(productDP[rows - 1][cols - 1][0], productDP[rows - 1][cols - 1][1])
        return -1 if result < 0 else result % (10 ** 9 + 7)