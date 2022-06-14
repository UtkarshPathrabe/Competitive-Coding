class Solution:
    def hammingWeight(self, n: int) -> int:
        bits, mask = 0, 1
        for i in range(32):
            if n & mask != 0:
                bits += 1
            mask <<= 1
        return bits