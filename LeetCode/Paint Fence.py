class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return k
        elif n == 2:
            return k * k
        else:
            prev01, prev02 = k, k * k
            n -= 2
            while n > 0:
                prev02, prev01 = (k - 1) * (prev02 + prev01), prev02
                n -= 1
            return prev02