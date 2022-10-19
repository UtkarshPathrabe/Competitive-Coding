class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freqMap = Counter(nums)
        result = [0, 0]
        for freq in freqMap.values():
            result[0] += freq // 2
            result[1] += freq % 2
        return result