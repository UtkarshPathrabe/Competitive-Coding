class Solution:
    def countBits(self, num: int) -> List[int]:
        result, i, b = [0] * (num + 1), 0, 1
        while b <= num:
            while i < b and i + b <= num:
                result[i + b] = result[i] + 1
                i += 1
            i, b = 0, b << 1
        return result