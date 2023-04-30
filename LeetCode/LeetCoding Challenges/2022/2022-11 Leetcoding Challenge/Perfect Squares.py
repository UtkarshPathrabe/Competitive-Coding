class Solution:
    def numSquares(self, n: int) -> int:
        while (n & 3) == 0:
            n >>= 2
        if (n & 7) == 7:
            return 4
        
        def isSquare(n):
            squareRoot = int(math.sqrt(n))
            return squareRoot * squareRoot == n
        
        if isSquare(n):
            return 1
        for i in range(1, int(math.sqrt(n)) + 1):
            if isSquare(n - (i*i)):
                return 2
        return 3