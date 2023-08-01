class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        adjList = defaultdict(list)
        for i in range(n):
            for node in graph[i]:
                adjList[node].append(i)
                indegree[i] += 1
        queue = deque()
        # Push all the nodes with indegree zero in the queue.
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        safe = [False] * n
        while queue:
            node = queue.popleft()
            safe[node] = True
            for neighbour in adjList[node]:
                # Delete the edge "node -> neighbour".
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        safeNodes = []
        for i in range(n):
            if safe[i]:
                safeNodes.append(i)
        return safeNodes