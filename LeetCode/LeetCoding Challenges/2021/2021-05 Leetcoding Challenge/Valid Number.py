class Solution:
    def isNumber(self, s: str) -> bool:
        seenDigit = seenExponent = seenDot = False
        for i, char in enumerate(s):
            if char.isdigit():
                seenDigit = True
            elif char in ['+', '-']:
                if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
            elif char in ['e', 'E']:
                if seenExponent or not seenDigit:
                    return False
                seenExponent, seenDigit = True, False
            elif char == '.':
                if seenDot or seenExponent:
                    return False
                seenDot = True
            else:
                return False
        return seenDigit