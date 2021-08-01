class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N, area, index = len(grid), {}, 2
        def neighbours(r, c):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc
        def dfs(r, c, index):
            result = 1
            grid[r][c] = index
            for nr, nc in neighbours(r, c):
                if grid[nr][nc] == 1:
                    result += dfs(nr, nc, index)
            return result
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1
        result = max(area.values() or [0])
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for nr, nc in neighbours(r, c) if grid[nr][nc] > 1}
                    result = max(result, 1 + sum(area[i] for i in seen))
        return result