class Solution:
    def minSteps(self, n: int) -> int:
        result, divisor = 0, 2
        while n > 1:
            while n % divisor == 0:
                result += divisor
                n /= divisor
            divisor += 1
        return result