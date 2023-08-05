class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        queue, visited, N = deque([(0, 0, 1)]), set((0, 0)), len(grid)
        while queue:
            r, c, d = queue.popleft()
            if r == N - 1 and c == N - 1:
                return d
            for row, col in [(r + 1, c), (r + 1, c + 1), (r, c + 1), (r - 1, c + 1), (r - 1, c), (r - 1, c - 1), (r, c - 1), (r + 1, c - 1)]:
                if 0 <= row < N and 0 <= col < N and grid[row][col] == 0 and (row, col) not in visited:
                    queue.append((row, col, d + 1))
                    visited.add((row, col))
        return -1