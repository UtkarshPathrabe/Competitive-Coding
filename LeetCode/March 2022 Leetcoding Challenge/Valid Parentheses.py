class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')':
                if not stack or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif c == '}':
                if not stack or stack[-1] != '{':
                    return False
                else:
                    stack.pop()
            elif c == ']':
                if not stack or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
        return len(stack) == 0