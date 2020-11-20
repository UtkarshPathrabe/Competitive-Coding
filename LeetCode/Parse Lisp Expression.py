class Solution:
    def __init__(self):
        self.scope = [{}]
    
    def evaluate(self, expression: str) -> int:
        self.scope.append({})
        result = self.evaluateInner(expression)
        self.scope.pop()
        return result
    
    def evaluateInner(self, expression):
        if expression[0] != '(':
            if expression[0].isdigit() or expression[0] == '-':
                return int(expression)
            for i in range(len(self.scope) - 1, -1, -1):
                if expression in self.scope[i]:
                    return self.scope[i][expression]
        tokens = self.parse(expression[5 + (expression[1] == 'm'): -1])
        if expression.startswith('(add'):
            return self.evaluate(tokens[0]) + self.evaluate(tokens[1])
        elif expression.startswith('(mult'):
            return self.evaluate(tokens[0]) * self.evaluate(tokens[1])
        else:
            for j in range(1, len(tokens), 2):
                self.scope[-1][tokens[j - 1]] = self.evaluate(tokens[j])
            return self.evaluate(tokens[-1])
    
    def parse(self, expression):
        result, balance, buffer = [], 0, []
        for token in expression.split():
            for char in token:
                if char == '(':
                    balance += 1
                if char == ')':
                    balance -= 1
            if len(buffer) > 0:
                buffer.append(' ')
            buffer.append(token)
            if balance == 0:
                result.append(''.join(buffer))
                buffer = []
        if len(buffer) > 0:
            result.append(''.join(buffer))
        return result