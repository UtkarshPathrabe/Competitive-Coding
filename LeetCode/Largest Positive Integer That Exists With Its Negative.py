class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        numsSet = set(nums)
        result = -1
        for num in nums:
            if (-1 * num) in numsSet:
                result = max(result, abs(num))
        return result