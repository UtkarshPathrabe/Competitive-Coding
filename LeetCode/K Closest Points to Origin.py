class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distanceSquare(point: List[int]):
            return (point[0] * point[0]) + (point[1] * point[1])
        heap = [(distanceSquare(point), (point[0], point[1])) for point in points]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]