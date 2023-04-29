class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for rowNumber in range(numRows):
            row = [None] * (rowNumber + 1)
            row[0], row[-1] = 1, 1
            for i in range(1, rowNumber):
                row[i] = triangle[rowNumber - 1][i - 1] + triangle[rowNumber - 1][i]
            triangle.append(row)
        return triangle