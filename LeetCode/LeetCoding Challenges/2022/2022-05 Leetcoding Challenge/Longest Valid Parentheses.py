class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result, stack = 0, deque([-1])
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    result = max(result, i - stack[-1])
        return result