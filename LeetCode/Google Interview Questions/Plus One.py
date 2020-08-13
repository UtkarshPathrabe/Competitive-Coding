class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for index in range(len(digits) - 1, -1, -1):
            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] += 1
                return digits
        return [1] + digits