class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        colCheckMap = defaultdict(set)
        for row in range(n):
            rowSet = set()
            for col in range(n):
                rowSet.add(matrix[row][col])
                colCheckMap[col].add(matrix[row][col])
            if len(rowSet) != n:
                return False
        for _, s in colCheckMap.items():
            if len(s) != n:
                return False
        return True