class Solution:
    def reverse(self, x: int) -> int:
        result = int('-' + str(abs(x))[::-1]) if x < 0 else int(str(x)[::-1])
        return 0 if abs(result) > (1 << 31) - 1 else result