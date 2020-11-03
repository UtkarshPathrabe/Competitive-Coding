class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        visited, graph = [False for _ in range(n)], defaultdict(set)
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)
        def dfs(i):
            for j in graph[i]:
                if not visited[j]:
                    visited[j] = True
                    dfs(j)
        visited[0] = True
        dfs(0)
        return all(visited)