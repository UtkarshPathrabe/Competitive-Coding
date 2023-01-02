class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        lenMap = defaultdict(int)
        def getDistanceSquare(p1, p2):
            return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
        lenMap[getDistanceSquare(p1, p2)] += 1
        lenMap[getDistanceSquare(p2, p3)] += 1
        lenMap[getDistanceSquare(p3, p4)] += 1
        lenMap[getDistanceSquare(p4, p1)] += 1
        lenMap[getDistanceSquare(p1, p3)] += 1
        lenMap[getDistanceSquare(p2, p4)] += 1
        return len(lenMap) == 2 and set(lenMap.values()) == set([2, 4])