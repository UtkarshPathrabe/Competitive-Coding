class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(r == 0 or c == 0 or matrix[r - 1][c - 1] == val for r, row in enumerate(matrix) for c, val in enumerate(row))