class Solution:
    def isArmstrong(self, n: int) -> bool:
        length = math.floor(math.log10(n)) + 1
        def sumOfKthPowerOfDigits(n: int, k: int) -> int:
            result = 0
            while n != 0:
                result += (n % 10) ** k
                n //= 10
            return result
        return sumOfKthPowerOfDigits(n, length) == n