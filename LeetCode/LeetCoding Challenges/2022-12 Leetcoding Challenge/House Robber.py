class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax, currMax = 0, 0
        for num in nums:
            currMax, prevMax = max(prevMax + num, currMax), currMax
        return currMax