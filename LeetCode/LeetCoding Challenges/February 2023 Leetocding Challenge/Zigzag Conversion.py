class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows, rowNumber, goingDown = [[] for _ in range(min(numRows, len(s)))], 0, False
        for char in s:
            rows[rowNumber].append(char)
            if rowNumber == 0 or rowNumber == numRows - 1:
                goingDown = not goingDown
            rowNumber += 1 if goingDown else -1
        return ''.join([''.join(x) for x in rows])