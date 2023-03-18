class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n == 3 ** round(math.log(n, 3)) if n > 0 else False