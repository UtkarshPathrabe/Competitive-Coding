class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        rows, cols = len(M), len(M[0])
        def getSmoothValue(r, c):
            validSlots, currentSum = 0, 0
            for row, col in [(r, c), (r - 1, c), (r - 1, c + 1), (r, c + 1), (r + 1, c + 1), (r + 1, c), (r + 1, c - 1), (r, c - 1), (r - 1, c - 1)]:
                if 0 <= row < rows and 0 <= col < cols:
                    validSlots += 1
                    currentSum += M[row][col]
            return math.floor(currentSum / validSlots)
        result = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                result[r][c] = getSmoothValue(r, c)
        return result