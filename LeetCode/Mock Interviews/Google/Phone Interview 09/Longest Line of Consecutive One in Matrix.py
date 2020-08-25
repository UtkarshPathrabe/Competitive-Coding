class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        rowsLength = len(M)
        if rowsLength == 0:
            return 0
        columnsLength = len(M[0])
        rows = defaultdict(int)
        cols = defaultdict(int)
        ad = defaultdict(int)
        dd = defaultdict(int)
        maxCount = 0
        for i in range(rowsLength):
            for j in range(columnsLength):
                if M[i][j] == 0:
                    rows[i] = cols[j] = ad[j + i] = dd[j - i] = 0
                else:
                    rows[i] += 1
                    cols[j] += 1
                    ad[j + i] += 1
                    dd[j - i] += 1
                    maxCount = max(maxCount, rows[i], cols[j], ad[j + i], dd[j - i])
        return maxCount