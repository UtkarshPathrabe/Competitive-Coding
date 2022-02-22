class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        memo = {1: [1]}
        def recurse(n):
            if n not in memo:
                odds = recurse((n + 1) // 2)
                evens = recurse(n // 2)
                memo[n] = [2 * x - 1 for x in odds] + [2 * x for x in evens]
            return memo[n]
        return recurse(n)