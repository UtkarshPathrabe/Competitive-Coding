class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        result = -1
        for i in range(len(A)):
            j = bisect.bisect_left(A, K - A[i], i + 1) - 1
            if j > i:
                result = max(result, A[i] + A[j])
        return result