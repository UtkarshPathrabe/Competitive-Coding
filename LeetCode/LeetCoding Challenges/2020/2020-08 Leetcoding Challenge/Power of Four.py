import math

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        else:
            if math.floor(log(abs(num), 4)) == math.ceil(log(abs(num), 4)):
                return True
            return False