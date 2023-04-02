class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        def bfs(startNode):
            queue = deque([startNode])
            visited = set()
            distance = [float('inf')] * n
            distance[startNode] = 0
            while queue:
                node = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                neighbour = edges[node]
                if neighbour != -1 and neighbour not in visited:
                    distance[neighbour] = 1 + distance[node]
                    queue.append(neighbour)
            return distance
        dist1 = bfs(node1)
        dist2 = bfs(node2)
        minimumDistanceNode, minimumDistanceTillNow = -1, float('inf')
        for cuurentNode in range(n):
            if minimumDistanceTillNow > max(dist1[cuurentNode], dist2[cuurentNode]):
                minimumDistanceNode = cuurentNode
                minimumDistanceTillNow = max(dist1[cuurentNode], dist2[cuurentNode])
        return minimumDistanceNode