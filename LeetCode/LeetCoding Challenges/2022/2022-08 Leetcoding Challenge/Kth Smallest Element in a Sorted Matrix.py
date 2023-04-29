class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def countLessEqual(mid, smaller, larger):
            count = 0
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] > mid:
                    larger, row = min(larger, matrix[row][col]), row - 1
                else:
                    smaller, count, col = max(smaller, matrix[row][col]), count + row + 1, col + 1
            return count, smaller, larger
        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]
        while start < end:
            mid = start + ((end - start) >> 1)
            smaller, larger = matrix[0][0], matrix[n - 1][n - 1]
            count, smaller, larger = countLessEqual(mid, smaller, larger)
            if count == k:
                return smaller
            if count < k:
                start = larger
            else:
                end = smaller
        return start