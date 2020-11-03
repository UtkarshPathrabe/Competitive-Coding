class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited, count, graph = [False for _ in range(n)], 0, defaultdict(set)
        def dfs(i):
            for j in graph[i]:
                if not visited[j]:
                    visited[j] = True
                    dfs(j)
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count