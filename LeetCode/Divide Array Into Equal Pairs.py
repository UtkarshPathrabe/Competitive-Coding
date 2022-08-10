class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freqMap = Counter(nums)
        for val in freqMap.values():
            if val % 2 == 1:
                return False
        return True