class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        count = Counter(str(N))
        return any(count == Counter(str(1 << b)) for b in range(31))