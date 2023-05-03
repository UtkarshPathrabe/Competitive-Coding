class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        graph = defaultdict(set)
        for node1, node2 in connections:
            graph[node1].add(node2)
            graph[node2].add(node1)
        noOfConnectedComponents, visited = 0, set()
        def dfs(node: int):
            visited.add(node)
            if node not in graph:
                return
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        for i in range(n):
            if i not in visited:
                noOfConnectedComponents += 1
                dfs(i)
        return noOfConnectedComponents - 1