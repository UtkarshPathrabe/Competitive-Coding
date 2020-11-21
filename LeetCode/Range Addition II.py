class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        rows, cols = m, n
        for a, b in ops:
            rows, cols = min(rows, a), min(cols, b)
        return rows * cols