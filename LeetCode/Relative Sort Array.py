class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freqMap = Counter(arr1)
        result = []
        for num in arr2:
            if num in freqMap:
                result.extend([num] * freqMap[num])
                freqMap.pop(num)
        for key in sorted(freqMap.keys()):
            result.extend([key] * freqMap[key])
        return result