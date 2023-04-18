class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diagonals, antiDiagonals):
            if row == n:
                return 1
            solutions = 0
            for col in range(n):
                currentDiagonal = row - col
                currentAntiDiagonal = row + col
                if (col in cols or currentDiagonal in diagonals or currentAntiDiagonal in antiDiagonals):
                    continue
                cols.add(col)
                diagonals.add(currentDiagonal)
                antiDiagonals.add(currentAntiDiagonal)
                solutions += backtrack(row + 1, cols, diagonals, antiDiagonals)
                cols.remove(col)
                diagonals.remove(currentDiagonal)
                antiDiagonals.remove(currentAntiDiagonal)
            return solutions
        return backtrack(0, set(), set(), set())