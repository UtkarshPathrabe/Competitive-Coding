class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        n = floor(log2(N)) + 1
        bitmask = (1 << n) - 1
        return bitmask ^ N