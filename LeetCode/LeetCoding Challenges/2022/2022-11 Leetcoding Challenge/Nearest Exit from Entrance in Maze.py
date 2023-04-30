class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited, queue = set([(entrance[0], entrance[1])]), deque([(entrance[0], entrance[1], 0)])
        while queue:
            x, y, steps = queue.popleft()
            if (x == 0 or y == 0 or x == (len(maze) - 1) or y == (len(maze[0]) - 1)) and steps > 0:
                return steps
            for nextX, nextY in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nextX < len(maze) and 0 <= nextY < len(maze[0]) and maze[nextX][nextY] == '.' and (nextX, nextY) not in visited:
                    visited.add((nextX, nextY))
                    queue.append((nextX, nextY, steps + 1))
        return -1