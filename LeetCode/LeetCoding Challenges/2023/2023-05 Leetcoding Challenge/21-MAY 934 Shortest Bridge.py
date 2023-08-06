class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        rows, cols = len(A), len(A[0])
        
        def neighbours(r, c):
            for row, col in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if 0 <= row < rows and 0 <= col < cols:
                    yield row, col
        
        def getComponents():
            visited, components = set(), []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val == 1 and (r, c) not in visited:
                        seen, stack = {(r, c)}, deque([(r, c),])
                        while stack:
                            node = stack.pop()
                            for nei in neighbours(*node):
                                if nei not in seen and A[nei[0]][nei[1]] == 1:
                                    seen.add(nei)
                                    stack.append(nei)
                        visited |= seen
                        components.append(seen)
            return components
        
        source, target = getComponents()
        queue, visited = deque([(node, 0) for node in source]), set(source)
        while queue:
            node, d = queue.popleft()
            if node in target:
                return d - 1
            for nei in neighbours(*node):
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, d + 1))