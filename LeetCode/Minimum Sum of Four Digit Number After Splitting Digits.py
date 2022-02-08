class Solution:
    def minimumSum(self, num: int) -> int:
        num1, num2, num3, num4 = list(map(int, sorted(str(num))))
        return (num1 + num2) * 10 + (num3 + num4)