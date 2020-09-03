class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(1 if stone in set(J) else 0 for stone in S)