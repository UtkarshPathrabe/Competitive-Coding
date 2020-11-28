class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        currentSum, currentFactor = 1, 1
        for i in range(n):
            currentFactor *= choices[i]
            currentSum += currentFactor
        return currentSum