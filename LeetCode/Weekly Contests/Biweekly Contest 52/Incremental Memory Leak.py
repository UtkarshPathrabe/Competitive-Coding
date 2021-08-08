class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        heap, requirement = [(-memory1, 1), (-memory2, 2)], 1
        heapq.heapify(heap)
        while requirement <= -heap[0][0]:
            memory, index = heapq.heappop(heap)
            memory += requirement
            heapq.heappush(heap, (memory, index))
            requirement += 1
        if heap[0][1] == 1:
            mem1, mem2 = -heap[0][0], -heap[1][0]
        else:
            mem1, mem2 = -heap[1][0], -heap[0][0]
        return [requirement, mem1, mem2]