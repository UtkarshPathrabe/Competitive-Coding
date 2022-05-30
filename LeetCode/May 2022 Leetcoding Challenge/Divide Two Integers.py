class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT, MIN_INT, HALF_MIN_INT = 2 ** 31 - 1, -2 ** 31, -2 ** 30
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor
        quotient = 0
        while divisor >= dividend:
            powerOfTwo = -1
            value = divisor
            while value >= HALF_MIN_INT and value + value >= dividend:
                value += value
                powerOfTwo += powerOfTwo
            quotient += powerOfTwo
            dividend -= value
        return -quotient if negatives != 1 else quotient