class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for char in num:
            while stack and k and stack[-1] > char:
                stack.pop()
                k -= 1
            if stack or char is not "0":
                stack.append(char)
        if k:
            stack = stack[0: -k]
        return "".join(stack) or "0"