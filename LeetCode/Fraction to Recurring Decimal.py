class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        fraction = []
        if (numerator < 0) ^ (denominator < 0):
            fraction.append('-')
        dividend, divisor = abs(numerator), abs(denominator)
        quotient, remainder = divmod(dividend, divisor)
        fraction.append(str(quotient))
        if remainder == 0:
            return ''.join(fraction)
        fraction.append('.')
        hashMap = {}
        while remainder:
            if str(remainder) in hashMap:
                fraction.insert(hashMap[str(remainder)], '(')
                fraction.append(')')
                break
            hashMap[str(remainder)] = len(fraction)
            remainder *= 10
            fraction.append(str(remainder // divisor))
            remainder %= divisor
        return ''.join(fraction)