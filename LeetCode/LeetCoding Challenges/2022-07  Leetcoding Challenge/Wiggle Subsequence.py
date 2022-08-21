class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        prevDiff = nums[1] - nums[0]
        count = 2 if prevDiff != 0 else 1
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prevDiff <= 0) or (diff < 0 and prevDiff >= 0):
                count, prevDiff = count + 1, diff
        return count