class Solution:
    def balancedStringSplit(self, s: str) -> int:
        frequency, result = 0, 0
        for char in s:
            frequency += 1 if char == 'L' else -1
            if frequency == 0:
                result += 1
        return result