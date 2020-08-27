class Solution:
    def isHappy(self, n: int) -> bool:
        def getNextNumber(n):
            nextNumber = 0
            while n > 0:
                n, digit = divmod(n, 10)
                nextNumber += digit ** 2
            return nextNumber
        seenSet = set()
        while n != 1 and n not in seenSet:
            seenSet.add(n)
            n = getNextNumber(n)
        return n == 1