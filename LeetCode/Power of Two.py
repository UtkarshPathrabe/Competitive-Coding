class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n == 2 ** round(math.log2(n)) if n > 0 else False