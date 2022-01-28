class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        l, r, result = 0, len(nums) - 1, 0
        nums.sort()
        while l < r:
            result += nums[r] - nums[l]
            l, r = l + 1, r - 1
        return result