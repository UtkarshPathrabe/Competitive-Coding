class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols, isFirstColZero = len(matrix), len(matrix[0]), False
        for row in range(rows):
            if matrix[row][0] == 0:
                isFirstColZero = True
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if col == 0 and isFirstColZero:
                    matrix[row][0] = 0
                if row == 0 and matrix[0][0] == 0:
                    matrix[0][col] = 0
                if col > 0 and row > 0 and (matrix[row][0] == 0 or matrix[0][col] == 0):
                    matrix[row][col] = 0