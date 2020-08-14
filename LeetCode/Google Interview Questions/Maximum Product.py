class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        numsLength = len(nums)
        if numsLength == 0:
            return 0
        maxSoFar = nums[0]
        minSoFar = nums[0]
        result = maxSoFar
        for i in range(1, numsLength):
            tempMax = max(nums[i], maxSoFar * nums[i], minSoFar * nums[i])
            tempMin = min(nums[i], minSoFar * nums[i], maxSoFar * nums[i])
            maxSoFar = tempMax
            minSoFar = tempMin
            result = max(result, maxSoFar)
        return result