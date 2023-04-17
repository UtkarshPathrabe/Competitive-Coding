class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        count, currentSum = 0, 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                count += 1
            else:
                currentSum += ((count + 1) * count) // 2
                count = 0
        currentSum += ((count + 1) * count) // 2
        return currentSum