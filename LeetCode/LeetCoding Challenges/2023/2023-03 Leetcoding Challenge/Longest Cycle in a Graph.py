class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        result, N = -1, len(edges)
        visited = [False] * N
        def dfs(node: int, distMap):
            nonlocal result
            visited[node] = True
            neighbour = edges[node]
            if neighbour != -1 and not visited[neighbour]:
                distMap[neighbour] = distMap[node] + 1
                dfs(neighbour, distMap)
            elif neighbour != -1 and neighbour in distMap:
                result = max(result, distMap[node] - distMap[neighbour] + 1)
        for i in range(N):
            if not visited[i]:
                distMap = {i: 1}
                dfs(i, distMap)
        return result