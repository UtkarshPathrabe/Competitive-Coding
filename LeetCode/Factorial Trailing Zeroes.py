class Solution:
    def trailingZeroes(self, n: int) -> int:
        factor, result = 5, 0
        while factor <= n:
            result += n // factor
            factor *= 5
        return result