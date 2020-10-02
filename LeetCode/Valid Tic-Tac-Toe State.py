class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        player1, player2, xCount, oCount = 'X', 'O', 0, 0
        for row in board:
            for val in row:
                if val == player1:
                    xCount += 1
                if val == player2:
                    oCount += 1
        
        def checkWin(player):
            nonlocal board
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
                if all(board[j][i] == player for j in range(3)):
                    return True
            return (player == board[0][0] == board[1][1] == board[2][2]) or (player == board[0][2] == board[1][1] == board[2][0])
        
        if oCount not in {xCount, xCount - 1}:
            return False
        if checkWin(player1) and xCount != oCount + 1:
            return False
        if checkWin(player2) and xCount != oCount:
            return False
        return True