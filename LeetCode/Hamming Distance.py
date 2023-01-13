class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        bitCount = 0
        for i in range(32):
            if (xor >> i) & 1 == 1:
                bitCount += 1
        return bitCount