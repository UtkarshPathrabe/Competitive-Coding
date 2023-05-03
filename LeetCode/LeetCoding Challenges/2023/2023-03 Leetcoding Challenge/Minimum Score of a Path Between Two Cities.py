class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        result, visited = float('inf'), set()
        for start, end, distance in roads:
            graph[start].append((end, distance))
            graph[end].append((start, distance))
        def dfs(node: int):
            nonlocal result
            visited.add(node)
            if node not in graph:
                return
            for neighbour, distance in graph[node]:
                result = min(result, distance)
                if neighbour not in visited:
                    dfs(neighbour)
        dfs(1)
        return result