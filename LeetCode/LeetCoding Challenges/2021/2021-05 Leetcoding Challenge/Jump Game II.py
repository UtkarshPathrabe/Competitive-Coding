class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        maxPos, maxSteps, jumps = nums[0], nums[0], 1
        for i in range(1, len(nums)):
            if maxSteps < i:
                jumps += 1
                maxSteps = maxPos
            maxPos = max(maxPos, i + nums[i])
        return jumps