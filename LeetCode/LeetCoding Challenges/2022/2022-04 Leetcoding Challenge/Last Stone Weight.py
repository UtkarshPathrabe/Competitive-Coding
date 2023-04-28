class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)
        while heap:
            s1 = -heapq.heappop(heap)
            if not heap:
                return s1
            s2 = -heapq.heappop(heap)
            if s1 > s2:
                heapq.heappush(heap, s2 - s1)
        return 0