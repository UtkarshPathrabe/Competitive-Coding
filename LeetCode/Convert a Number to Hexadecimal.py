class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        chars, result = '0123456789abcdef', []
        if num < 0:
            num += (1 << 32)
        while num > 0:
            result.insert(0, chars[num % 16])
            num //= 16
        return ''.join(result)