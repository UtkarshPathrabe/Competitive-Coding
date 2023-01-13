class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        def checkBit(num, i):
            return (num >> i) & 1 == 1
        msb = 32
        for i in range(32, -1, -1):
            if checkBit(n, i):
                msb = i
                break
        for i in range(msb, 0, -1):
            if checkBit(n, i) ^ checkBit(n, i - 1) == 0:
                return False
        return True