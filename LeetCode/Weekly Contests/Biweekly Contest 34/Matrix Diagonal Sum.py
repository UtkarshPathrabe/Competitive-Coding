class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        currentSum, n = 0, len(mat)
        for i in range(n):
            currentSum += mat[i][i]
            if i != n - i - 1:
                currentSum += mat[i][n - i - 1]
        return currentSum