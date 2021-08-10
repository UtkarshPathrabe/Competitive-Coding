class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nextNumber, result = nums[0] + 1, 0
        for i in range(1, len(nums)):
            if nextNumber > nums[i]:
                result += (nextNumber - nums[i])
                nextNumber += 1
            else:
                nextNumber = nums[i] + 1
        return result