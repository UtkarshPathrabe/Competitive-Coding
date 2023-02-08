class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        maxPos, maxSteps, jumps = nums[0], nums[0], 1
        for i in range(1, len(nums)):
            # if we have come to the end of the current jump,
            # we need to make another jump
            if maxSteps < i:
                jumps += 1
                maxSteps = maxPos
            # we continuously find the how far we can reach in the current jump
            maxPos = max(maxPos, i + nums[i])
        return jumps