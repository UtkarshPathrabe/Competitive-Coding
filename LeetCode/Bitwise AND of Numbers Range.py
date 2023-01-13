class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        n = right
        while n > left:
            n &= (n - 1)
        return left & n