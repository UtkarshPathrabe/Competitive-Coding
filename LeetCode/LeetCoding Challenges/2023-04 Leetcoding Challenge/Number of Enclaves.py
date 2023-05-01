class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols, visited = len(grid), len(grid[0]), set()
        DIRX = [0, 1, 0, -1]
        DIRY = [-1, 0, 1, 0]
        def bfs(x, y):
            queue = deque([(x, y)])
            visited.add((x, y))
            while queue:
                row, col = queue.popleft()
                for i in range(4):
                    r, c = row + DIRX[i], col + DIRY[i]
                    if r < 0 or r >= rows or c < 0 or c >= cols:
                        continue
                    elif grid[r][c] == 1 and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))
        for i in range(rows):
            # First Column
            if grid[i][0] == 1 and (i, 0) not in visited:
                bfs(i, 0)
            # Last Column
            if grid[i][cols - 1] == 1 and (i, cols - 1) not in visited:
                bfs(i, n - 1)
        for i in range(cols):
            # First Row
            if grid[0][i] == 1 and (0, i) not in visited:
                bfs(0, i)
            # Last Row
            if grid[rows - 1][i] == 1 and (rows - 1, i) not in visited:
                bfs(rows - 1, i)
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    count += 1
        return count
