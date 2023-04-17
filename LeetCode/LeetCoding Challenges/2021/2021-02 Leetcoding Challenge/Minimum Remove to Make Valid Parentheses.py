class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, indicesToRemove, result = [], set(), []
        for i, c in enumerate(s):
            if c not in ['(', ')']:
                continue
            if c == '(':
                stack.append(i)
            elif not stack:
                indicesToRemove.add(i)
            else:
                stack.pop()
        indicesToRemove = indicesToRemove.union(set(stack))
        for i, c in enumerate(s):
            if i not in indicesToRemove:
                result.append(c)
        return ''.join(result)