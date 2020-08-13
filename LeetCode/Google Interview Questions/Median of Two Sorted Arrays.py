class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError
        iMin, iMax, halfLength = 0, m, (m + n + 1) // 2
        while iMin <= iMax:
            i = (iMin + iMax) // 2
            j = halfLength - i
            if i < m and B[j - 1] > A[i]:
                iMin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                iMax = i - 1
            else:
                if i == 0:
                    maxOfLeft = B[j - 1]
                elif j == 0:
                    maxOfLeft = A[i - 1]
                else:
                    maxOfLeft = max(A[i - 1], B[j - 1])
                if (m + n) % 2 == 1:
                    return maxOfLeft
                if i == m:
                    minOfRight = B[j]
                elif j == n:
                    minOfRight = A[i]
                else:
                    minOfRight = min(A[i], B[j])
                return (maxOfLeft + minOfRight) / 2.0