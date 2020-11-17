class Solution:
    def convertToTitle(self, n: int) -> str:
        result = []
        while n:
            result.append(chr(ord('A') + ((n - 1) % 26)))
            n = (n - 1) // 26
        return ''.join(result[::-1])