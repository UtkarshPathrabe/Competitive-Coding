class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for index, num in enumerate(nums):
            if len(heap) == k:
                heappushpop(heap, (num, index))
            else:
                heappush(heap, (num, index))
        return [t[0] for t in sorted(heap, key = lambda x : x[1])]