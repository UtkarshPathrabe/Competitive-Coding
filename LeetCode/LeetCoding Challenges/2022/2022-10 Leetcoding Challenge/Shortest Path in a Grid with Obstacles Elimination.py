class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        # [1] this check significantly improves runtime, i.e., we can use path (0,0) -> (0,n-1) -> (m-1,n-1)
        if k >= (m + n - 2):
            return m + n - 2
        # (x, y, obstacles we can destroy, steps done so far)
        dequeue = deque([(0, 0, k, 0)])
        seen = set()
        while dequeue:
            row, col, remaining, steps = dequeue.popleft()
            if (row, col) == (m - 1, n - 1):
                return steps
            for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if 0 <= r < m and 0 <= c < n and remaining >= grid[r][c]:
                    step = (r, c, remaining - grid[r][c], steps + 1)
                    if step[0:3] not in seen:
                        seen.add(step[0:3])
                        dequeue.append(step)
        return -1