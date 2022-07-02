MAX_VALUE = 100000
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def isValid(point: List[int]) -> bool:
            return point[0] == x or point[1] == y
        def getManhattanDistance(point: List[int]) -> int:
            return abs(point[0] - x) + abs(point[1] - y)
        minDist = MAX_VALUE
        result = -1
        for index, point in enumerate(points):
            if isValid(point):
                dist = getManhattanDistance(point)
                if dist < minDist:
                    minDist = dist
                    result = index
        return result