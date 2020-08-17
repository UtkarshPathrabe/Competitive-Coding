class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        WHITE = 1
        GRAY = 2
        BLACK = 3
        adjacencyList = defaultdict(list)
        for destination, source in prerequisites:
            adjacencyList[source].append(destination)
        color = {node: WHITE for node in range(numCourses)}
        topologicalSortedOrder = []
        isValid = True
        def dfs(node):
            nonlocal isValid, topologicalSortedOrder, color, adjacencyList
            if not isValid:
                return
            color[node] = GRAY
            if node in adjacencyList:
                for destination in adjacencyList[node]:
                    if color[destination] == WHITE:
                        dfs(destination)
                    elif color[destination] == GRAY:
                        isValid = False
            color[node] = BLACK
            topologicalSortedOrder.append(node)
        for node in range(numCourses):
            if color[node] == WHITE:
                dfs(node)
        return topologicalSortedOrder[::-1] if isValid else []