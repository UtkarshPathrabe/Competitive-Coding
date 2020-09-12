class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for index in range(n):
            result ^= (start + 2 * index)
        return result