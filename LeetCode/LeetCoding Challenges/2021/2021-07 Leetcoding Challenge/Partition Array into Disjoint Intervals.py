class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        currentMax, leftMax, solution = nums[0], nums[0], 1
        for i in range(1, len(nums)):
            if currentMax > nums[i]:
                solution, currentMax = i + 1, leftMax
            else:
                leftMax = max(leftMax, nums[i])
        return solution