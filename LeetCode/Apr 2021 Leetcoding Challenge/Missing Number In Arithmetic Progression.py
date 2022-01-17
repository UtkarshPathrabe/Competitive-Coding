class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        difference, low, high = (arr[n - 1] - arr[0]) // n, 0, n - 1
        while low < high:
            mid = low + ((high - low) >> 1)
            if arr[mid] == (arr[0] + mid * difference):
                low = mid + 1
            else:
                high = mid
        return arr[0] + low * difference