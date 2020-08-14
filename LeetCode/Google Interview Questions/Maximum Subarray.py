class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        numsLength = len(nums)
        maxSum = nums[0]
        for i in range(1, numsLength):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            maxSum = max(maxSum, nums[i])
        return maxSum