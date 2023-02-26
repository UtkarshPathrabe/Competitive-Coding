class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.size = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.antiDiagonal = 0
        self.playerToken = {1: 1, 2: -1}

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        token = self.playerToken[player]
        self.rows[row] += token
        self.cols[col] += token
        if row == col:
            self.diagonal += token
        if self.size - row - 1 == col:
            self.antiDiagonal += token
        if self.size * token in [self.rows[row], self.cols[col], self.diagonal, self.antiDiagonal]:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)