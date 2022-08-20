class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freqMap = Counter(nums)
        result = 0
        for key, value in freqMap.items():
            if value == 1:
                result += key
        return result