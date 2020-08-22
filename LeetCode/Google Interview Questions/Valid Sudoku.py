class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]
        for row in range(9):
            for column in range(9):
                num = board[row][column]
                if num != '.':
                    num = int(num)
                    boxIndex = ((row // 3) * 3) + (column // 3)
                    rows[row][num] = rows[row].get(num, 0) + 1
                    columns[column][num] = columns[column].get(num, 0) + 1
                    boxes[boxIndex][num] = boxes[boxIndex].get(num, 0) + 1
                    if rows[row][num] > 1 or columns[column][num] > 1 or boxes[boxIndex][num] > 1:
                        return False
        return True