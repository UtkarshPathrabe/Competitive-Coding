class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        countMap = Counter(nums)
        frequencyArray = [(freq, item) for item, freq in countMap.items()]
        frequencyArray.sort(key = lambda x : (x[0], -x[1]))
        result = []
        for x in frequencyArray:
            for _ in range(x[0]):
                result.append(x[1])
        return result