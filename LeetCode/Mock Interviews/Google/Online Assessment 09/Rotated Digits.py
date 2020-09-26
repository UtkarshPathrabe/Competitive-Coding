class Solution:
    def rotatedDigits(self, N: int) -> int:
        A = list(map(int, str(N)))
        memo = {}
        def dp(i, equalityFlag, involutionFlag):
            if i == len(A):
                return +(involutionFlag)
            if (i, equalityFlag, involutionFlag) not in memo:
                result = 0
                for d in range(A[i] + 1 if equalityFlag else 10):
                    if d in {3, 4, 7}:
                        continue
                    result += dp(i + 1, equalityFlag and d == A[i], involutionFlag or d in {2, 5, 6, 9})
                memo[(i, equalityFlag, involutionFlag)] = result
            return memo[(i, equalityFlag, involutionFlag)]
        return dp(0, True, False)