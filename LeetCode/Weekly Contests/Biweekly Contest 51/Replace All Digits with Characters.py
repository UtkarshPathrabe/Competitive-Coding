class Solution:
    def replaceDigits(self, s: str) -> str:
        l, N = list(s), len(s)
        for i in range(1, N, 2):
            l[i] = chr(ord(l[i - 1]) + int(l[i]))
        return ''.join(l)