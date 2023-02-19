class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) >> 1
            if mid + citations[mid] >= n:
                right = mid - 1
            else:
                left = mid + 1
        return n - left