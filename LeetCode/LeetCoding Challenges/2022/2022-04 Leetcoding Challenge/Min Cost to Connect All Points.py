class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        getDist = lambda p1, p2: abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
        numberOfPoints = len(points)
        parent, heap, edgesCovered, cost = [-1] * numberOfPoints, [], 0, 0
        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            parent[py] = px
        for p1 in range(numberOfPoints):
            for p2 in range(p1 + 1, numberOfPoints):
                heap.append((getDist(points[p1], points[p2]), p1, p2))
        heapify(heap)
        while edgesCovered < numberOfPoints - 1:
            d, p1, p2 = heappop(heap)
            if find(p1) != find(p2):
                cost += d
                edgesCovered += 1
                union(p1, p2)
        return cost