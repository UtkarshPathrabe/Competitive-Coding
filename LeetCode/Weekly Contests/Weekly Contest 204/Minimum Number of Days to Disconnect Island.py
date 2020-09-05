class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        rows, cols = len(grid), len(grid[0])
        
        def dfs(grid, visited, x, y):
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == 0 or visited[x][y]:
                return False
            visited[x][y] = True
            for direction in DIRECTIONS:
                dfs(grid, visited, x + direction[0], y + direction[1])
            return True
        
        def isDisconnected(grid):
            islands = 0
            visited = [[False] * cols for _ in range(rows)]
            for i in range(rows):
                for j in range(cols):
                    if dfs(grid, visited, i, j):
                        islands += 1
            return islands != 1
        
        def isStronglyConnected(grid):
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] != 0:
                        grid[i][j] = 0
                        if isDisconnected(grid):
                            return False
                        grid[i][j] = 1
            return True
        
        if isDisconnected(grid):
            return 0
        elif isStronglyConnected(grid):
            return 2
        else:
            return 1