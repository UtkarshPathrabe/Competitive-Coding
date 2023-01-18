class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum, result = 0, nums[0]
        for num in nums:
            currentSum = max(currentSum, 0) + num
            result = max(result, currentSum)
        return result