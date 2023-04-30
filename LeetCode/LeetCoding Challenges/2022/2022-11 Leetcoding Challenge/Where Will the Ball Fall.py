class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def helper(row, col):
            if row == len(grid):
                return col
            nextColumn = col + grid[row][col]
            if nextColumn < 0 or nextColumn >= len(grid[0]) or grid[row][col] != grid[row][nextColumn]:
                return -1
            return helper(row + 1, nextColumn)
        result = [-1] * len(grid[0])
        for i in range(len(grid[0])):
            result[i] = helper(0, i)
        return result