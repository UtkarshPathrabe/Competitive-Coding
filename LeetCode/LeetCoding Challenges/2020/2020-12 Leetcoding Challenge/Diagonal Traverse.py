class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        rows, cols, result, directionUp = len(matrix), len(matrix[0]), [], True
        for currentSum in range(rows + cols - 1):
            if directionUp:
                if currentSum < rows:
                    row, col = currentSum, 0
                else:
                    row, col = rows - 1, currentSum - rows + 1
                while row > -1 and col < cols:
                    result.append(matrix[row][col])
                    row -= 1
                    col += 1
            else:
                if currentSum < cols:
                    row, col = 0, currentSum
                else:
                    row, col = currentSum - cols + 1, cols - 1
                while col > -1 and row < rows:
                    result.append(matrix[row][col])
                    row += 1
                    col -= 1
            directionUp = not directionUp
        return result