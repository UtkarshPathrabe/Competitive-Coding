class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sequence, base, result = '123456789', 10, []
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(base - length):
                number = int(sequence[start : start + length])
                if low <= number <= high:
                    result.append(number)
        return result