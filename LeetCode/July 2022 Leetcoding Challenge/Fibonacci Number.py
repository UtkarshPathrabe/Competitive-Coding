class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n in [1, 2]:
            return 1
        fib = [1, 1, 2]
        for i in range(3, n + 1):
            fib[(i - 1) % 3] = fib[i % 3] + fib[(i + 1) % 3]
        return fib[(i - 1) % 3]