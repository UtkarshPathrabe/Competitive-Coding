class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        for num in nums[1:]:
            result.append(result[-1] + num)
        return result