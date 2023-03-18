import math

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        else:
            log4 = log(abs(num), 4)
            if math.floor(log4) == math.ceil(log4):
                return True
            return False