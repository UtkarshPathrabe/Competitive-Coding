class Solution:
    def maxDepth(self, s: str) -> int:
        depth = maxDepth = 0
        for char in s:
            if char == '(':
                depth += 1
                maxDepth = max(maxDepth, depth)
            elif char == ')':
                depth -= 1
        return maxDepth