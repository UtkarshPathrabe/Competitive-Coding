class Solution:
    def judgeCircle(self, moves: str) -> bool:
        frequency = Counter(moves)
        return frequency.get('U', 0) == frequency.get('D', 0) and frequency.get('L', 0) == frequency.get('R', 0)