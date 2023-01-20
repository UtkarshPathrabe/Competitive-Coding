class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        MOVES = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]
        visited, queue = set(), deque([(0, 0, 0)])
        while queue:
            currentX, currentY, depth = queue.popleft()
            if currentX == x and currentY == y:
                return depth
            for move in MOVES:
                nextX, nextY = currentX + move[0], currentY + move[1]
                if (nextX, nextY) not in visited:
                    visited.add((nextX, nextY))
                    queue.append((nextX, nextY, depth + 1))