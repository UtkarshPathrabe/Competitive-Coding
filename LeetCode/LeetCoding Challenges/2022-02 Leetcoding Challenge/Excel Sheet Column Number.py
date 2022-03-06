class Solution:
    def titleToNumber(self, s: str) -> int:
        columnNumber = 0
        exponentialPower = 0
        for i in range(len(s) - 1, -1 , -1):
            columnNumber += ((26 ** exponentialPower) * (ord(s[i]) - ord('A') + 1))
            exponentialPower += 1
        return columnNumber