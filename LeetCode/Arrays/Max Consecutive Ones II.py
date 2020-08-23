class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        flipIndex, count, maxLength, numsCapacity = -1, 0, 0, len(nums)
        for i in range(numsCapacity):
            if nums[i] == 1:
                count += 1
            elif flipIndex < 0:
                flipIndex = i
                count += 1
            else:
                maxLength = max(count, maxLength)
                count = i - flipIndex
                flipIndex = i
        return max(count, maxLength)