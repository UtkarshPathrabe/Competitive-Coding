class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        for x1, y1 in points:
            counter = defaultdict(int)
            for x2, y2 in points:
                if x2 == x1 and y2 == y1:
                    continue
                counter[(x2 - x1) ** 2 + (y2 - y1) ** 2] += 1
            for k in counter.values():
                if k > 1:
                    result += k * (k - 1)
        return result