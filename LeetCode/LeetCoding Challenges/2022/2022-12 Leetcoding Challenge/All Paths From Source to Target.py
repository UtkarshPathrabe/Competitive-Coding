class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        def dfs(node, currentPath):
            if node == len(graph) - 1:
                result.append(currentPath[:])
                return
            for neighbour in graph[node]:
                dfs(neighbour, currentPath + [neighbour])
        dfs(0, [0])
        return result