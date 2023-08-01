class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength, start, end, currentSum = 10000000, 0, 0, 0
        while end < len(nums):
            currentSum += nums[end]
            end += 1
            while currentSum >= target:
                minLength = min(end - start, minLength)
                currentSum -= nums[start]
                start += 1
        return minLength if minLength != 10000000 else 0