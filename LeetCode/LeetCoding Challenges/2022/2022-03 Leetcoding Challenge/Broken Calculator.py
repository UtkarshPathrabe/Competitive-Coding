class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        result = 0
        while Y > X:
            result += 1
            if Y % 2:
                Y += 1
            else:
                Y //= 2
        return result + X - Y