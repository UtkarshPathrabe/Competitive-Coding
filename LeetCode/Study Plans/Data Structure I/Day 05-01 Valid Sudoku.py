class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [defaultdict(int) for _ in range(9)]
        cols = [defaultdict(int) for _ in range(9)]
        boxes = [defaultdict(int) for _ in range(9)]
        for row in range(9):
            for col in range(9):
                boxIndex = ((row // 3) * 3) + (col // 3)
                if board[row][col] != '.':
                    number = int(board[row][col])
                    rows[row][number] += 1
                    cols[col][number] += 1
                    boxes[boxIndex][number] += 1
                    if rows[row][number] > 1 or cols[col][number] > 1 or boxes[boxIndex][number] > 1:
                        return False
        return True