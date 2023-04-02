class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        arrayLength = len(A)
        i = 0
        while i + 1 < arrayLength and A[i] < A[i + 1]:
            i += 1
        if i == 0 or i == arrayLength - 1:
            return False
        while i + 1 < arrayLength and A[i] > A[i + 1]:
            i += 1
        return i == arrayLength - 1