class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        special, rows, cols = 0, len(mat), len(mat[0])
        for row in range(rows):
            countOfOneInRow = mat[row].count(1)
            if countOfOneInRow == 1:
                countOfOneInCol = 0
                indexOfOne = mat[row].index(1)
                for i in range(rows):
                    if mat[i][indexOfOne] == 1:
                        countOfOneInCol += 1
                if countOfOneInCol == 1:
                    special += 1
        return special