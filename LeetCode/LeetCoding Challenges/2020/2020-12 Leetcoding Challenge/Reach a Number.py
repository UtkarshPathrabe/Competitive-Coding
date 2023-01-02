class Solution:
    def reachNumber(self, target: int) -> int:
        target, k = abs(target), 0
        while target > 0:
            k += 1
            target -= k
        return k if target % 2 == 0 else k + 1 + k % 2