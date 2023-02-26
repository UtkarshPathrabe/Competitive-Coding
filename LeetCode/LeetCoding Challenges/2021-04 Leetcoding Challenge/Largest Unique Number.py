class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        freqMap = Counter(A)
        for key in sorted(freqMap, reverse = True):
            if freqMap[key] == 1:
                return key
        return -1