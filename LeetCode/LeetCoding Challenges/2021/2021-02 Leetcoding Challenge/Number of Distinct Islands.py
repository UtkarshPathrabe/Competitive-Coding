class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        uniqueIslands, visited, rowHead, colHead, currentIsland = set(), set(), float('-inf'), float('-inf'), set()
        def dfsHelper(row, col):
            visited.add((row, col))
            currentIsland.add((row - rowHead, col - colHead))
            for r, c in [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]:
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1 and (r, c) not in visited:
                    dfsHelper(r, c)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    rowHead, colHead, currentIsland = row, col, set()
                    dfsHelper(row, col)
                    if currentIsland:
                        uniqueIslands.add(frozenset(currentIsland))
        return len(uniqueIslands)