class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0
        result, lastNumber, currentNumber, operation = 0, 0, 0, '+'
        for i, char in enumerate(s):
            if char.isdigit():
                currentNumber = (currentNumber * 10) + int(char)
            if not char.isdigit() and char != ' ' or i == len(s) - 1:
                if operation == '+' or operation == '-':
                    result += lastNumber
                    lastNumber = currentNumber if operation == '+' else -1 * currentNumber
                elif operation == '*':
                    lastNumber *= currentNumber
                elif operation == '/':
                    lastNumber = int(lastNumber / currentNumber)
                operation = char
                currentNumber = 0
        result += lastNumber
        return result