class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(k):
            val = heapq.heappop(nums)
            heapq.heappush(nums, -val)
        return sum(nums)