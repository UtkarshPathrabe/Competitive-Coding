class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length, result = 1, 0
        while length <= len(arr):
            for start in range(len(arr) - length + 1):
                result += sum(arr[start : start + length])
            length += 2
        return result