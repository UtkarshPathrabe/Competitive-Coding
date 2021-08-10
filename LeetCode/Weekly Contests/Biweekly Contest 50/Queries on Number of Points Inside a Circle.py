class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        return [len([p for p in points if pow(p[0] - q[0], 2) + pow(p[1] - q[1], 2) <= pow(q[2], 2)]) for q in queries]