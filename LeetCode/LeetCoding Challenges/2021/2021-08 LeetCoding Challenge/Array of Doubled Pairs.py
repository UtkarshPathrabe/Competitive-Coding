class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        freqMap = Counter(arr)
        for x in sorted(arr, key = abs):
            if freqMap[x] == 0:
                continue
            if freqMap[2 * x] == 0:
                return False
            freqMap[x], freqMap[2 * x] = freqMap[x] - 1, freqMap[2 * x] - 1
        return True