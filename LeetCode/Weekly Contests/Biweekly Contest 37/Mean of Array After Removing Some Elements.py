class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        arrLength = len(arr)
        return sum(arr[int(0.05 * arrLength): int(0.95 * arrLength)]) / int(0.9 * arrLength)