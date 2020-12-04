class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, currentSum = 1, 0
        while n > 0:
            n, d = divmod(n, 10)
            product *= d
            currentSum += d
        return product - currentSum