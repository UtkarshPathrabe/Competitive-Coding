class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        negative = num < 0
        num, result, chars = abs(num), [], '0123456'
        while num > 0:
            result.insert(0, chars[num % 7])
            num //= 7
        return ('-' if negative else '') + ''.join(result)