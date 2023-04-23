class Solution:
    def myAtoi(self, s: str) -> int:
        sign, number, index, sLen = 1, 0, 0, len(s)
        while index < sLen and s[index] == ' ':
            index += 1
        if index < sLen and (s[index] == '+' or s[index] == '-'):
            sign = -1 if s[index] == '-' else 1
            index += 1
        while index < sLen and s[index].isdigit():
            number = number * 10 + (ord(s[index]) - ord('0'))
            index += 1
        if (sign * number) > 2**31 - 1:
            return 2**31 - 1
        elif (sign * number) < -1 * (2**31):
            return -1 * (2**31)
        else:
            return (sign * number)