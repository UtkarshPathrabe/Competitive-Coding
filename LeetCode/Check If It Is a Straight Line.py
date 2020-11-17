class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) in [0, 1, 2]:
            return True
        def getSlope(x, y):
            if y[1] - x[1] == 0:
                return 0
            elif y[0] - x[0] == 0:
                return float('inf')
            else:
                return ((y[1] - x[1]) / (y[0] - x[0]))
        slope = getSlope(coordinates[0], coordinates[1])
        for i in range(2, len(coordinates)):
            if slope != getSlope(coordinates[i - 1], coordinates[i]):
                return False
        return True