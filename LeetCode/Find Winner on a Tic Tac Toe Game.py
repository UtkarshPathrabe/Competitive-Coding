class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [['.' for _ in range(3)] for _ in range(3)]
        for index, move in enumerate(moves):
            if index % 2 == 0:
                board[move[0]][move[1]] = 'A'
            else:
                board[move[0]][move[1]] = 'B'
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '.':
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '.':
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
            return board[0][2]
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'