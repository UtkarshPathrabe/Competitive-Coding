class Solution:
    def minOperations(self, n: int) -> int:
        count, result = n - 1, 0
        while count > 0:
            result += count
            count -= 2
        return result