class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        WHITE, GRAY, BLACK = 0, 1, 2
        def buildDigraph():
            graph = [[] for _ in range(n)]
            for src, dst in edges:
                graph[src].append(dst)
            return graph
        def dfsHelper(node, states):
            if states[node] != WHITE:
                return states[node] == BLACK
            if len(graph[node]) == 0:
                return node == destination
            states[node] = GRAY
            for nextNode in graph[node]:
                if not dfsHelper(nextNode, states):
                    return False
            states[node] = BLACK
            return True
        graph = buildDigraph()
        return dfsHelper(source, [WHITE] * n)