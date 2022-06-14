class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        numberOfRows = len(matrix)
        result = 0
        if numberOfRows == 0:
            return result
        numberOfColumns = len(matrix[0])
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        resultCache = []
        for _ in range(numberOfRows):
            resultCache.append([0 for _ in range(numberOfColumns)])
        
        def dfs(matrix, row, column):
            nonlocal numberOfRows, numberOfColumns, resultCache
            if resultCache[row][column] != 0:
                return resultCache[row][column]
            for rowDirection, columnDirection in DIRECTIONS:
                newRow, newColumn = row + rowDirection, column + columnDirection
                if 0 <= newRow and newRow < numberOfRows and 0 <= newColumn and newColumn < numberOfColumns and matrix[newRow][newColumn] > matrix[row][column]:
                    resultCache[row][column] = max(resultCache[row][column], dfs(matrix, newRow, newColumn))
            resultCache[row][column] += 1
            return resultCache[row][column]
        
        for row in range(numberOfRows):
            for column in range(numberOfColumns):
                result = max(result, dfs(matrix, row, column))
        return result