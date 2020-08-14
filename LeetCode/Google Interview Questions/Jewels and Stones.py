class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewelsSet = set(J)
        return sum(1 if stone in jewelsSet else 0 for stone in S)