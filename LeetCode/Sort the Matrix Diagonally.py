class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        if rows == 0:
            return mat
        cols = len(mat[0])
        elementMap = defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                elementMap[c - r].append(mat[r][c])
        for element in elementMap.keys():
            elementMap[element].sort()
        for r in range(rows):
            for c  in range(cols):
                mat[r][c] = elementMap[c - r].pop(0)
        return mat