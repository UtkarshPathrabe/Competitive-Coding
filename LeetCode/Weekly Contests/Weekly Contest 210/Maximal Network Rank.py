class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adjMatrix, degree, maxNetworkRank = [[0] * n for _ in range(n)], [0] * n, 0
        for a, b in roads:
            adjMatrix[a][b] = adjMatrix[b][a] = 1
            degree[a] += 1
            degree[b] += 1
        for i in range(n):
            for j in range(i + 1, n):
                maxNetworkRank = max(maxNetworkRank, degree[i] + degree[j] - adjMatrix[i][j])
        return maxNetworkRank