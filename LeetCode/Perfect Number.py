class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        currentSum, i = 1, 2
        while i * i <= num:
            if num % i == 0:
                currentSum += i
                if i * i != num:
                    currentSum += (num / i)
            i += 1
        return currentSum == num