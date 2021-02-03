class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        result, mod = 1, 1337
        a %= mod
        for num in b:
            result = (((result ** 10) % mod) * ((a ** num) % mod)) % mod
        return result