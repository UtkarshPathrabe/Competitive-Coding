class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            for char in str(num):
                if char == '0' or num % int(char) != 0:
                    break
            else:
                result.append(num)
        return result