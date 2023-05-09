class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1
        for num in nums:
            if num > 0:
                result *= 1
            elif num < 0:
                result *= -1
            else:
                result *= 0
            if result == 0:
                return 0
        return result