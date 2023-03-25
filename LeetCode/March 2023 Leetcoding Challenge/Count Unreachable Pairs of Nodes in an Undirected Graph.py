class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        visited, numberOfPairs, remainingNodes, sizeOfComponent = set(), 0, n, 0
        for edgeStart, edgeEnd in edges:
            graph[edgeStart].add(edgeEnd)
            graph[edgeEnd].add(edgeStart)
        def dfs(node):
            count = 1
            visited.add(node)
            if node not in graph:
                return count
            for neighbour in graph[node]:
                if neighbour not in visited:
                    count += dfs(neighbour)
            return count
        for i in range(n):
            if i not in visited:
                sizeOfComponent = dfs(i)
                numberOfPairs += sizeOfComponent * (remainingNodes - sizeOfComponent)
                remainingNodes -= sizeOfComponent
        return numberOfPairs