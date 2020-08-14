class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pointsSet = set(map(tuple, points))
        pointsLength = len(points)
        minArea = float('inf')
        for i in range(pointsLength):
            for j in range(i + 1, pointsLength):
                p1, p2 = points[i], points[j]
                if p1[0] != p2[0] and p1[1] != p2[1] and (p1[0], p2[1]) in pointsSet and (p2[0], p1[1]) in pointsSet:
                    minArea = min(minArea, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
        return minArea if minArea < float('inf') else 0