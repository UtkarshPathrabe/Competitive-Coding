class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result, n = 0, len(grid)
        # Keep track of the frequency of each row.
        rowCounter = collections.Counter(tuple(row) for row in grid)
        # Add up the frequency of each column in map.
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            result += rowCounter[tuple(col)]
        return result