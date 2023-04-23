class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numberMap = dict()
        for i, num in enumerate(nums):
            complementNumber = target - num
            if complementNumber in numberMap:
                return [numberMap[complementNumber], i]
            numberMap[num] = i
        return []