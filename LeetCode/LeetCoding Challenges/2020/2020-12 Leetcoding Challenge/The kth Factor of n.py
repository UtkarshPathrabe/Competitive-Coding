class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        divisors, sqrt = [], int(n ** 0.5)
        for i in range(1, sqrt + 1):
            if n % i == 0:
                k -= 1
                divisors.append(i)
                if k == 0:
                    return i
        if sqrt * sqrt == n:
            k += 1
        numberOfDivisors = len(divisors)
        return n // divisors[numberOfDivisors - k] if k <= numberOfDivisors else -1