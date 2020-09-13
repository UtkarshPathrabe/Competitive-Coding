class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        primitiveEndIndices = set([0])
        count = 0
        for i, char in enumerate(S):
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            if count == 0:
                primitiveEndIndices.add(i)
                primitiveEndIndices.add(i + 1)
        result = []
        for i in range(len(S)):
            if i not in primitiveEndIndices:
                result.append(S[i])
        return ''.join(result)