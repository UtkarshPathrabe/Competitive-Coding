class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if token == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b + a)
            elif token == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            elif token == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b * a)
            elif token == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b / a)
            else:
                stack.append(token)
        return int(stack.pop())