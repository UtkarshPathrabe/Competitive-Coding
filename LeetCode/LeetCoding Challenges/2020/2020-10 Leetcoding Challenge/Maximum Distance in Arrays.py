class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        result, minValue, maxValue = 0, arrays[0][0], arrays[0][-1]
        for array in arrays[1:]:
            result = max(result, abs(maxValue - array[0]), abs(array[-1] - minValue))
            minValue = min(minValue, array[0])
            maxValue = max(maxValue, array[-1])
        return result