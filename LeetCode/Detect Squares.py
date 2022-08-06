class DetectSquares:

    def __init__(self):
        self.freqMap = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.freqMap[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        candidateX, candidateY = set(), set()
        for p in self.freqMap:
            if p[0] == point[0] and (p[0], p[1]) not in candidateY:
                candidateY.add(p)
            if p[1] == point[1] and (p[0], p[1]) not in candidateX:
                candidateX.add(p)
        result = 0
        for x in candidateX:
            for y in candidateY:
                if abs(point[0] - x[0]) > 0 and abs(point[0] - x[0]) == abs(point[1] - y[1]) and (x[0], y[1]) in self.freqMap:
                    result += (self.freqMap[x] * self.freqMap[y] * self.freqMap[(x[0], y[1])])
        return result


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)