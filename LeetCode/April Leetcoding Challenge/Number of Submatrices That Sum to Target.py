class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r, c = len(matrix), len(matrix[0])
        ps = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + matrix[i - 1][j - 1]
        count = 0
        for r1 in range(1, r + 1):
            for r2 in range(r1, r + 1):
                s = defaultdict(int)
                s[0] = 1
                for col in range(1, c + 1):
                    currentSum = ps[r2][col] - ps[r1 - 1][col]
                    count += s[currentSum - target]
                    s[currentSum] += 1
        return count