class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD, freqMap, maximumElement, result = 10**9 + 7, Counter(nums), max(nums), 0
        prefixFreq = [0] * (maximumElement + 1)
        for num in range(1, maximumElement + 1):
            prefixFreq[num] = prefixFreq[num - 1] + freqMap[num]
        for num in freqMap.keys():
            for i in range(num, maximumElement + 1, num):
                result = (result + freqMap[num] * (prefixFreq[-1] - prefixFreq[i - 1])) % MOD
        return result % MOD