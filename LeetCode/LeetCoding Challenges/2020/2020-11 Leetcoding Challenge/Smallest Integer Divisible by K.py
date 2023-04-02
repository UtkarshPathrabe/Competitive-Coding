class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        remainder = 0
        for NLength in range(1, K + 1):
            remainder = (remainder * 10 + 1) % K
            if remainder == 0:
                return NLength
        return -1