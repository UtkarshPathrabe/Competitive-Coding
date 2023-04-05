class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result, prefixSum = 0, 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            result = max(result, math.ceil(prefixSum / (i + 1)))
        return result