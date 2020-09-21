class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        numberOfRows = numberOfColumns = len(matrix)
        for i in range(numberOfRows):
            for j in range(i, numberOfColumns):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        for i in range(numberOfRows):
            matrix[i].reverse()