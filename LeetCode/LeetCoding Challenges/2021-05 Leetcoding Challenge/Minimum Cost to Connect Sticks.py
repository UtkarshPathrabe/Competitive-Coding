class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        totalCost, pq = 0, []
        for stick in sticks:
            heapq.heappush(pq, stick)
        while len(pq) > 1:
            stick1, stick2 = heapq.heappop(pq), heapq.heappop(pq)
            heapq.heappush(pq, stick1 + stick2)
            totalCost += stick1 + stick2
        return totalCost