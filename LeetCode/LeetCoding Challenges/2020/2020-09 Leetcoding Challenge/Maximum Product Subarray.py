class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxSoFar = minSoFar = result = nums[0]
        for num in nums[1:]:
            maxSoFar, minSoFar = max(num, maxSoFar * num, minSoFar * num), min(num, maxSoFar * num, minSoFar * num)
            result = max(maxSoFar, result)
        return result