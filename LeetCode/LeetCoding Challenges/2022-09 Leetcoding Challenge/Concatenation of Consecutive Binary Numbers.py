class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD, length, result = 10 ** 9 + 7, 0, 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                length += 1
            result = ((result << length) | i) % MOD
        return result