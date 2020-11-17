class Solution:
    def encode(self, num: int) -> str:
        if num == 0:
            return ''
        remainder, divisor, count = num, 1, 0
        while remainder >= divisor:
            remainder -= divisor
            count += 1
            divisor *= 2
        return bin(remainder)[2:].zfill(count)