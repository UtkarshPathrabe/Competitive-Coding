class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if len(a) == 1:
            return True
        if a[:2] == b[-2:][::-1]:
            return True
        if a[-2:][::-1] == b[:2]:
            return True
        return False