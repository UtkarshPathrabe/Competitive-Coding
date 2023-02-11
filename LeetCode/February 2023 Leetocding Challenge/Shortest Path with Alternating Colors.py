class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for redEdge in redEdges:
            graph[redEdge[0]].append((redEdge[1], 0))
        for blueEdge in blueEdges:
            graph[blueEdge[0]].append((blueEdge[1], 1))
        result = [-1] * n
        visited = set()
        # Start with node 0, with number of steps as 0 and undefined color -1.
        queue = deque([(0, 0, -1)])
        result[0] = 0
        visited.add((0, 0))
        visited.add((0, 1))
        while queue:
            node, steps, prevColor = queue.popleft()
            if node not in graph:
                continue
            for neighbour, color in graph[node]:
                if (neighbour, color) not in visited and color != prevColor:
                    if result[neighbour] == -1:
                        result[neighbour] = steps + 1
                    visited.add((neighbour, color))
                    queue.append((neighbour, steps + 1, color))
        return result