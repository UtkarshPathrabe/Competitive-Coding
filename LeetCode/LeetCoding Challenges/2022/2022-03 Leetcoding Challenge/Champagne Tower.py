class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * k for k in range(1, 102)]
        tower[0][0] = poured
        for row in range(query_row + 1):
            for col in range(row + 1):
                remaining = (tower[row][col] - 1.0) / 2.0
                if remaining > 0:
                    tower[row + 1][col] += remaining
                    tower[row + 1][col + 1] += remaining
        return min(1, tower[query_row][query_glass])