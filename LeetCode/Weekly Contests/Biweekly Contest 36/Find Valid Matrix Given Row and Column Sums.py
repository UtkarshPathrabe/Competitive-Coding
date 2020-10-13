class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        numberOfRows, numberOfColumns = len(rowSum), len(colSum)
        matrix = [[0] * numberOfColumns for _ in range(numberOfRows)]
        for row in range(numberOfRows):
            for col in range(numberOfColumns):
                matrix[row][col] = min(rowSum[row], colSum[col])
                rowSum[row] -= matrix[row][col]
                colSum[col] -= matrix[row][col]
        return matrix