class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            b = math.sqrt(c - int(a * a))
            if b == int(b):
                return True
            a += 1
        return False