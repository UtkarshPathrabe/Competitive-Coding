class Solution:
    def makeGood(self, s: str) -> str:
        stack = deque()
        for char in s:
            if stack and stack[-1].lower() == char.lower() and ((char.isupper() and stack[-1].islower()) or (char.islower() and stack[-1].isupper())):
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)