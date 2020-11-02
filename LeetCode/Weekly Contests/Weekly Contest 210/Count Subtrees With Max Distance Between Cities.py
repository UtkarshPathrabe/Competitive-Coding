class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[float('inf') for _ in range(n)] for _ in range(n)]
        for u, v in edges:
            graph[u - 1][v - 1] = graph[v - 1][u - 1] = 1
        for k, i, j in permutations(range(n), 3):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        result = [0 for _ in range(n - 1)]
        for numberOfVertices in range(2, n + 1):
            for subset in combinations(range(n), numberOfVertices):
                directEdgesInvolved = sum(graph[i][j] for i, j in combinations(subset, 2) if graph[i][j] == 1)
                maxDistance = max(graph[i][j] for i, j in combinations(subset, 2))
                if directEdgesInvolved == numberOfVertices - 1:
                    result[maxDistance - 1] += 1
        return result