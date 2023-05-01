class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque([])
        for char in s:
            if char != '*':
                stack.append(char)
            elif len(stack) > 0:
                stack.pop()
        return ''.join(stack)