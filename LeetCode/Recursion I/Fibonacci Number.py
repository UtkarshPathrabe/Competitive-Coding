class Solution:
    def fib(self, N: int) -> int:
        cache = {0: 0, 1: 1}
        def fibHelper(N):
            if N in cache:
                return cache[N]
            cache[N] = fibHelper(N - 1) + fibHelper(N - 2)
            return cache[N]
        return fibHelper(N)