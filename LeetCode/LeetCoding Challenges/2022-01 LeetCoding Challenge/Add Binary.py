class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lenA, lenB, carry = len(a), len(b), 0
        pA, pB, result = lenA - 1, lenB - 1, []
        while pA >= 0 or pB >= 0:
            xA, xB = int(a[pA]) if pA >= 0 else 0, int(b[pB]) if pB >= 0 else 0
            currentSum = xA + xB + carry
            carry = currentSum >> 1
            result.insert(0, str(currentSum % 2))
            pA, pB = pA - 1, pB - 1
        if carry:
            result.insert(0, str(carry))
        return ''.join(result)