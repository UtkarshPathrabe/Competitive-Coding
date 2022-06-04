class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def createBoard(state):
            board = []
            for row in state:
                board.append(''.join(row))
            return board
        def backtrack(row, columns, diagonals, antiDiagonals, state):
            if row == n:
                result.append(createBoard(state))
                return
            for col in range(n):
                diagonal = row - col
                antiDiagonal = row + col
                if col in columns or diagonal in diagonals or antiDiagonal in antiDiagonals:
                    continue
                columns.add(col)
                diagonals.add(diagonal)
                antiDiagonals.add(antiDiagonal)
                state[row][col] = 'Q'
                backtrack(row + 1, columns, diagonals, antiDiagonals, state)
                columns.remove(col)
                diagonals.remove(diagonal)
                antiDiagonals.remove(antiDiagonal)
                state[row][col] = '.'
        result = []
        emptyBoard = [['.'] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), emptyBoard)
        return result