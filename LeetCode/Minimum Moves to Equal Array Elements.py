class Solution:
    def minMoves(self, nums: List[int]) -> int:
        result, minNum = 0, min(nums)
        for num in nums:
            result += num - minNum
        return result