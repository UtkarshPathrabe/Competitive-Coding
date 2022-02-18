class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        pacificSet = set([(0, i) for i in range(n)]) | set([(i, 0) for i in range(1, m)])
        atlanticSet = set([(m - 1, i) for i in range(n)]) | set([(i, n - 1) for i in range(0, m - 1)])
        def expandSetUsingBFS(providedSet):
            visited, queue = set(), deque(providedSet)
            while queue:
                r, c = queue.popleft()
                visited.add((r, c))
                for row, col in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= row < m and 0 <= col < n and (row, col) not in visited and matrix[row][col] >= matrix[r][c]:
                        queue.append((row, col))
            return visited
        
        return expandSetUsingBFS(pacificSet) & expandSetUsingBFS(atlanticSet)