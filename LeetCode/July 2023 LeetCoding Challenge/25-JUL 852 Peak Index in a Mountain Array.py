class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        low = 0
        high = len(A) - 1
        while low < high:
            mid = low + ((high - low) >> 1)
            if A[mid] < A[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return low