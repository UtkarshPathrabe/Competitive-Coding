class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPower(x, n):
            if n == 0:
                return float(1)
            temp = fastPower(x, n // 2)
            if n % 2:
                return float(temp * temp * x)
            else:
                return float(temp * temp)
        if n < 0:
            x = 1 / x
            n = -n
        return fastPower(x, n)