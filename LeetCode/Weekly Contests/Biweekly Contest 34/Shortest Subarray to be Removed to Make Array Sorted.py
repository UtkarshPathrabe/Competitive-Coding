class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return 0
        last = n - 1
        while last > 0 and arr[last - 1] <= arr[last]:
            last -= 1
        result = last
        for i in range(n):
            if i > 0 and arr[i] < arr[i - 1]:
                break
            while last < n and (last <= i or arr[last] < arr[i]):
                last += 1
            result = min(result, last - i - 1)
        return result