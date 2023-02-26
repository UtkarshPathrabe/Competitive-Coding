class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        charIndex, result = float('-inf'), [float('inf')] * len(s)
        for i, char in enumerate(s):
            if char == c:
                charIndex, result[i] = i, 0
            else:
                result[i] = min(result[i], i - charIndex)
        charIndex = float('inf')
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                charIndex, result[i] = i, 0
            else:
                result[i] = min(result[i], charIndex - i)
        return result