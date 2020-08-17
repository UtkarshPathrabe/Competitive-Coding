class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencyList = defaultdict(list)
        nodeInDegree = {}
        for destination, source in prerequisites:
            adjacencyList[source].append(destination)
            nodeInDegree[destination] = nodeInDegree.get(destination, 0) + 1
        zeroInDegreeQueue = deque([node for node in range(numCourses) if node not in nodeInDegree])
        topologicalSort = []
        while zeroInDegreeQueue:
            node = zeroInDegreeQueue.popleft()
            topologicalSort.append(node)
            if node in adjacencyList:
                for neighbour in adjacencyList[node]:
                    nodeInDegree[neighbour] -= 1
                    if nodeInDegree[neighbour] == 0:
                        zeroInDegreeQueue.append(neighbour)
        return topologicalSort if len(topologicalSort) == numCourses else []