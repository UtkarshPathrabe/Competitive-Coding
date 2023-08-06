class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def getNumberOfDifferentWaysUsingFirstElementAsRoot(nums):
            if len(nums) <= 2:
                return 1
            leftElements = [num for num in nums[1:] if num < nums[0]]
            rightElements = [num for num in nums[1:] if num > nums[0]]
            return comb(len(leftElements) + len(rightElements), len(rightElements)) * getNumberOfDifferentWaysUsingFirstElementAsRoot(leftElements) * getNumberOfDifferentWaysUsingFirstElementAsRoot(rightElements)
        
        return (getNumberOfDifferentWaysUsingFirstElementAsRoot(nums) - 1) % (10**9 + 7)