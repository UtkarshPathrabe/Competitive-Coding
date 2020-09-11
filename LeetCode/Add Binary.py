class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1, n2, carry = len(a), len(b), 0
        p1, p2, result = n1 - 1, n2 - 1, []
        while p1 >= 0 or p2 >= 0:
            x1 = int(a[p1]) if p1 >= 0 else 0
            x2 = int(b[p2]) if p2 >= 0 else 0
            s = x1 + x2 + carry
            carry = s // 2
            result.insert(0, str(s % 2))
            p1 -= 1
            p2 -= 1
        if carry:
            result.insert(0, str(carry))
        return ''.join(result)