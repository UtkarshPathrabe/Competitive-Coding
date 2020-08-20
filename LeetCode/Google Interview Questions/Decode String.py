class Solution:
    def decodeString(self, s: str) -> str:
        result = ''
        currentNumber = 0
        stack = deque()
        for char in s:
            if char.isdigit():
                if currentNumber == 0:
                    currentNumber = int(char)
                else:
                    currentNumber = currentNumber * 10 + int(char)
            elif char.isalpha():
                result += char
            elif char == '[':
                stack.append((result, currentNumber))
                result = ''
                currentNumber = 0
            elif char == ']':
                topElement = stack.pop()
                result = topElement[0] + topElement[1] * result
        return result