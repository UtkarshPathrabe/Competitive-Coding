class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(lambda:1)
        for right in range(len(nums)):
            for left in range(right):
                diff = nums[right] - nums[left]
                dp[(right, diff)] = dp[(left, diff)] + 1
        return max(dp.values())