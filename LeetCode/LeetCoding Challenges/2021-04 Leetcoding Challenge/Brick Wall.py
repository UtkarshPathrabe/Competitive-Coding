class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps = defaultdict(int)
        for row in wall:
            position = 0
            for brick in row[:-1]:
                position += brick
                gaps[position] += 1
        fewestCrossings = len(wall)
        if len(gaps) > 0:
            fewestCrossings -= max(gaps.values())
        return fewestCrossings