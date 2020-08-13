class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPosition = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPosition:
                lastPosition = i
        return lastPosition == 0