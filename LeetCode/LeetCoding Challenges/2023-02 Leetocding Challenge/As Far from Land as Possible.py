class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        queue = deque([])
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    queue.append((i, j))
                    visited.add((i, j))
        distance = -1
        while queue:
            queueSize = len(queue)
            # Iterate over all the current cells in the queue.
            while queueSize:
                queueSize -= 1
                landCell = queue.popleft()
                # From the current land cell, traverse to all the four directions
                # and check if it is a water cell. If yes, convert it to land
                # and add it to the queue.
                for direction in DIRECTIONS:
                    x, y = landCell[0] + direction[0], landCell[1] + direction[1]
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and ((x, y) not in visited):
                        # Marking as 1 to avoid re-iterating it.
                        visited.add((x, y))
                        queue.append((x, y))
            distance += 1
        return -1 if distance == 0 else distance