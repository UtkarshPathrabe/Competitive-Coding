class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax, currMin, currSum, maxSum, minSum = 0, 0, 0, nums[0], nums[0]
        for num in nums:
            currMax = max(currMax, 0) + num
            maxSum = max(currMax, maxSum)
            currMin = min(currMin, 0) + num
            minSum = min(currMin, minSum)
            currSum += num
        return maxSum if minSum == currSum else max(maxSum, currSum - minSum)