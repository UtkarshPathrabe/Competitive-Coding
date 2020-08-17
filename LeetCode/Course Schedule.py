class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacencyList = defaultdict(list)
        nodeInDegree = {}
        totalEdges = 0
        for destination, source in prerequisites:
            adjacencyList[source].append(destination)
            nodeInDegree[destination] = nodeInDegree.get(destination, 0) + 1
            totalEdges += 1
        zeroInDegreeQueue = deque([node for node in range(numCourses) if node not in nodeInDegree])
        edgesTraversed = 0
        while zeroInDegreeQueue:
            node = zeroInDegreeQueue.popleft()
            for neighbour in adjacencyList[node]:
                nodeInDegree[neighbour] -= 1
                edgesTraversed += 1
                if nodeInDegree[neighbour] == 0:
                    zeroInDegreeQueue.append(neighbour)
        return edgesTraversed == totalEdges