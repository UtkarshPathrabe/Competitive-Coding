class Solution:
    def calculate(self, s: str) -> int:
        stack, exponent, operand = deque(), 0, 0
        def evaluateExpression():
            nonlocal stack
            result = stack.pop()
            while stack and stack[-1] != ')':
                sign = stack.pop()
                if sign == '+':
                    result += stack.pop()
                elif sign == '-':
                    result -= stack.pop()
            return result
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char.isdigit():
                operand = ((10 ** exponent) * int(char)) + operand
                exponent += 1
            elif char != ' ':
                if exponent:
                    stack.append(operand)
                    exponent, operand = 0, 0
                if char == '(':
                    result = evaluateExpression()
                    stack.pop()
                    stack.append(result)
                else:
                    stack.append(char)
        if exponent:
            stack.append(operand)
        return evaluateExpression()