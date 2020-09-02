class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        return 0 if sum([int(digit) for digit in str(min(A))]) % 2 else 1