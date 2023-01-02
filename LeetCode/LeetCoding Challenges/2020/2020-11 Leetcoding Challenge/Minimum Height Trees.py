class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        graph = defaultdict(set)
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)
        oneDegreeNodes, remainingNodes = deque([]), n
        for i in range(n):
            if len(graph[i]) == 1:
                oneDegreeNodes.append(i)
        while remainingNodes > 2:
            remainingNodes -= len(oneDegreeNodes)
            newOneDegreeNodes = deque([])
            while oneDegreeNodes:
                node = oneDegreeNodes.popleft()
                for neighbour in graph[node]:
                    graph[neighbour].remove(node)
                    if len(graph[neighbour]) == 1:
                        newOneDegreeNodes.append(neighbour)
            oneDegreeNodes = newOneDegreeNodes
        return oneDegreeNodes