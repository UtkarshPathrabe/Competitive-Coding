class Solution:
    def longestMountain(self, A: List[int]) -> int:
        result = base = 0
        while base < len(A):
            end = base
            if end + 1 < len(A) and A[end] < A[end + 1]:
                while end + 1 < len(A) and A[end] < A[end + 1]:
                    end += 1
                if end + 1 < len(A) and A[end] > A[end + 1]:
                    while end + 1 < len(A) and A[end] > A[end + 1]:
                        end += 1
                    result = max(result, end - base + 1)
            base = max(end, base + 1)
        return result