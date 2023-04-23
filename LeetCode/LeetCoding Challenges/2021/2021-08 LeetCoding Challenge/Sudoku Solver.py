class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        boxSize = 3
        gameSize = boxSize * boxSize
        
        def boxIndex(row, column):
            return ((row // boxSize) * boxSize) + (column // boxSize)
        
        rows = [defaultdict(int) for _ in range(gameSize)]
        columns = [defaultdict(int) for _ in range(gameSize)]
        boxes = [defaultdict(int) for _ in range(gameSize)]
        solved = False
        
        def canPlace(num, row, column):
            return num not in rows[row] and num not in columns[column] and num not in boxes[boxIndex(row, column)]
        
        def placeNumber(num, row, column):
            rows[row][num] += 1
            columns[column][num] += 1
            boxes[boxIndex(row, column)][num] += 1
            board[row][column] = str(num)
        
        def removeNumber(num, row, column):
            del rows[row][num]
            del columns[column][num]
            del boxes[boxIndex(row, column)][num]
            board[row][column] = '.'
            
        def placeNextNumber(row, column):
            if column == gameSize - 1 and row == gameSize - 1:
                nonlocal solved
                solved = True
            else:
                if column == gameSize - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, column + 1)
        
        def backtrack(row = 0, column = 0):
            if board[row][column] == '.':
                for i in range(1, 10):
                    if canPlace(i, row, column):
                        placeNumber(i, row, column)
                        placeNextNumber(row, column)
                        if not solved:
                            removeNumber(i, row, column)
            else:
                placeNextNumber(row, column)
        
        for row in range(gameSize):
            for column in range(gameSize):
                if board[row][column] != '.':
                    num = int(board[row][column])
                    placeNumber(num, row, column)
        backtrack()