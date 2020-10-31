class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        anchor, length = 0, 0
        for i in range(len(nums)):
            if i and nums[i - 1] >= nums[i]:
                anchor = i
            length = max(length, i - anchor + 1)
        return length