class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-1 * pile for pile in piles]
        heapq.heapify(heap)
        for i in range(k):
            maxPile = -1 * heapq.heappop(heap)
            newPile = maxPile - math.floor(maxPile / 2)
            heapq.heappush(heap, -1 * newPile)
        return -1 * sum(heap)