class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        count, result = Counter(), 0
        for row in grid:
            for c1, v1 in enumerate(row):
                if v1:
                    for c2 in range(c1 + 1, len(row)):
                        if row[c2]:
                            result += count[c1, c2]
                            count[c1, c2] += 1
        return result