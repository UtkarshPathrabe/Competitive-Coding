class Solution:
    def grayCode(self, n: int) -> List[int]:
        result, length = [], 1 << n
        for i in range(length):
            result.append(i ^ (i >> 1))
        return result