from heapq import *

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        self._heap = nums
        heapify(self._heap)

    def add(self, val: int) -> int:
        heappush(self._heap, val)
        while len(self._heap) > self._k:
            heappop(self._heap)
        return self._heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)