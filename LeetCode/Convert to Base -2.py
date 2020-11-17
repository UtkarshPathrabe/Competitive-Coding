class Solution:
    def baseNeg2(self, N: int) -> str:
        result = []
        while N:
            r = N % -2
            if r == -1:
                r = 1
            result.append(str(r))
            N = (N - r) // (-2)
        return ''.join(result[::-1]) or '0'