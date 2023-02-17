class Solution:
    def isUgly(self, num: int) -> bool:
        for i in (2, 3, 5):
            while num % i == 0 and num > 1:
                num //= i
        return num == 1