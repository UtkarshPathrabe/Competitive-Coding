class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = 0
        for i in range(len(number)):
            if number[i] == digit:
                result = max(result, int(number[0:i] + number[i+1:]))
        return str(result)