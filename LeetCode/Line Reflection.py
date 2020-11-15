class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points = sorted(set((i, j) for i, j in points))
        middle = round((points[0][0] + points[-1][0]) / 2, 2)
        leftPoints = list(filter(lambda x : x[0] < middle, points))
        rightPoints = list(filter(lambda x : x[0] > middle, points))
        if len(leftPoints) != len(rightPoints):
            return False
        rightPoints.sort(key = lambda x : -x[0])
        for l, r in zip(leftPoints, rightPoints):
            if not (l[0] + r[0] == middle * 2 and l[1] == r[1]):
                return False
        return True