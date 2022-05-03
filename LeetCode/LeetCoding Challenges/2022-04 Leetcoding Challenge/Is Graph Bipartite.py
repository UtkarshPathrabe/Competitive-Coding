class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodeColor = [None for _ in range(len(graph))]
        for node in range(len(graph)):
            if nodeColor[node] is None:
                stack = deque([node,])
                nodeColor[node] = 0
                while stack:
                    tempNode = stack.pop()
                    for neighbour in graph[tempNode]:
                        if nodeColor[neighbour] is None:
                            stack.append(neighbour)
                            nodeColor[neighbour] = nodeColor[tempNode] ^ 1
                        elif nodeColor[neighbour] == nodeColor[tempNode]:
                            return False
        return True