class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNumber, result = max(nums), -1
        for index, num in enumerate(nums):
            if maxNumber == num:
                result = index
            elif maxNumber < (2 * num):
                return -1
        return result