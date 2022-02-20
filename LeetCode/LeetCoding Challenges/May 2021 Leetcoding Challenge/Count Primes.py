class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        isPrime = [True] * n
        isPrime[0], isPrime[1] = False, False
        for i in range(2, math.ceil(math.sqrt(n))):
            if not isPrime[i]:
                continue
            for j in range(i * i, n, i):
                isPrime[j] = False
        return sum(isPrime)