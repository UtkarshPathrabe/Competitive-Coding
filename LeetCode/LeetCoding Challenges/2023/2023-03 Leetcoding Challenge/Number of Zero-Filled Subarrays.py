class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        def countSubArrays(size: int):
            return (size * (size + 1)) // 2
        result, currentZeroCount = 0, 0
        for num in nums:
            if num == 0:
                currentZeroCount += 1
            else:
                result += countSubArrays(currentZeroCount)
                currentZeroCount = 0
        return result + countSubArrays(currentZeroCount)