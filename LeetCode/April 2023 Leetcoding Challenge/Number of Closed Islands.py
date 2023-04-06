class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols, visited, count = len(grid), len(grid[0]), set(), 0
        DIRX = [0, 1, 0, -1]
        DIRY = [-1, 0, 1, 0]

        def bfs(row: int, col: int) -> bool:
            queue = deque([(row, col)])
            visited.add((row, col))
            isClosed = True
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    r, c = x + DIRX[i], y + DIRY[i]
                    if r < 0 or r >= rows or c < 0 or c >= cols:
                        # (x, y) is a boundary cell
                        isClosed = False
                    elif grid[r][c] == 0 and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))
            return isClosed
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and (row, col) not in visited and bfs(row, col):
                    count += 1
        return count