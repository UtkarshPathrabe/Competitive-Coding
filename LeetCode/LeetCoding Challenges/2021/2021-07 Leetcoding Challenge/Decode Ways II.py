class Solution:
    def numDecodings(self, s: str) -> int:
        M = 10 ** 9 + 7
        first, second = 1, 9 if s[0] == '*' else 0 if s[0] == '0' else 1
        for i in range(1, len(s)):
            temp = second
            if s[i] == '*':
                second = (9 * second) % M
                if s[i - 1] == '1':
                    second = (second + 9 * first) % M
                elif s[i - 1] == '2':
                    second = (second + 6 * first) % M
                elif s[i - 1] == '*':
                    second = (second + 15 * first) % M
            else:
                second = second if s[i] != '0' else 0
                if s[i - 1] == '1':
                    second = (second + first) % M
                elif s[i - 1] == '2' and s[i] <= '6':
                    second = (second + first) % M
                elif s[i - 1] == '*':
                    second = (second + (2 if s[i] <= '6' else 1) * first) % M
            first = temp
        return second