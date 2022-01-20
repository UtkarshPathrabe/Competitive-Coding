class Solution:
    def numberOfSteps (self, num: int) -> int:
        binary = bin(num)[2:]
        ones = binary.count("1")
        total = len(binary)
        return ones + total - 1