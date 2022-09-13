class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            complementNumber = target - num
            if complementNumber in hashMap:
                return [hashMap[complementNumber], i]
            hashMap[num] = i
        return []