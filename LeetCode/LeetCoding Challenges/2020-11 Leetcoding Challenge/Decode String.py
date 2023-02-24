class Solution:
    def decodeString(self, s: str) -> str:
        result, stack, currentCount = '', deque(), ''
        for char in s:
            if char.isdigit():
                currentCount += char
            elif char.isalpha():
                result += char
            elif char == '[':
                stack.append((result, int(currentCount)))
                result, currentCount = '', ''
            elif char == ']':
                oldResult, count = stack.pop()
                result = oldResult + count * result
        return result