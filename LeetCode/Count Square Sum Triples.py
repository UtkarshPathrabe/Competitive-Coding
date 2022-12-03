class Solution:
    def countTriples(self, n: int) -> int:
        result = 0
        for i in range(1, n + 1):
            for j in range (1, n + 1):
                rootSumOfSquare = sqrt(i * i + j * j)
                if rootSumOfSquare == math.floor(rootSumOfSquare) and rootSumOfSquare <= n:
                    result += 1
        return result