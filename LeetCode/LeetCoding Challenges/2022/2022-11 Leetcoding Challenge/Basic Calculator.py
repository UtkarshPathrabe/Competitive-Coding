class Solution:
    def calculate(self, s: str) -> int:
        # number is the current number we are constructing, initialize it with 0
        # sign is the '+' or '-' before the current number, initialize it with 1 to represent '+'
        # the number we are updating is the last element in the stack, initialize it with 0
        number, sign, stack = 0, 1, [0]
        for char in s:
            if char == ' ':
                continue
            elif char.isdigit():
                number = number * 10 + int(char)
            elif char == '+':
                stack[-1] += number * sign
                sign, number = 1, 0
            elif char == '-':
                stack[-1] += number * sign
                sign, number = -1, 0
            # we add sign to stack which represent sign of stuff inside ()
            # we also add 0 to stack so that we can keep it updating while evaluating the expression inside ()
            # reset number and sign again
            elif char == '(':
                stack.extend([sign, 0])
                sign, number = 1, 0
            # pop the last element and combine it with the current number and sign we are holding
            # pop the last element again which is the sign for '()' and multiply them together
            # add everything we get inside this '()' to the last element in the stack
            elif char == ')':
                lastNumber = (stack.pop() + number * sign) * stack.pop()
                stack[-1] += lastNumber
                sign, number = 1, 0
        # stack should only contain one element representing everything except the last number if the expression ended with a number, so add the current num we are holding to the result
        return stack[-1] + number * sign