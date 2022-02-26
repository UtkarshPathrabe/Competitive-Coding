class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        from fractions import gcd
        g = gcd(p, q)
        p, q = (p / g) % 2, (q / g) % 2
        return 1 if p and q else 0 if p else 2