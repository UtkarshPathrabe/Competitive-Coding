class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = sum(num for num in A if num % 2 == 0)
        result = []
        for val, index in queries:
            if A[index] % 2 == 0:
                evenSum -= A[index]
            A[index] += val
            if A[index] % 2 == 0:
                evenSum += A[index]
            result.append(evenSum)
        return result