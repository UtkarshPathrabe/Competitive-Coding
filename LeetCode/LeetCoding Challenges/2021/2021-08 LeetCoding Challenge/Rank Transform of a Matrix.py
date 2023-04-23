class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols, valIndexMap = len(matrix), len(matrix[0]), defaultdict(list)
        rank = [0 for _ in range(rows + cols)]
        for row in range(rows):
            for col in range(cols):
                valIndexMap[matrix[row][col]].append((row, col))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        for val in sorted(valIndexMap):
            parent, rankCopy = list(range(rows + cols)), rank[:]
            for i, j in valIndexMap[val]:
                i, j = find(i), find(j + rows)
                parent[i] = j
                rankCopy[j] = max(rankCopy[i], rankCopy[j])
            for i, j in valIndexMap[val]:
                rank[i] = rank[j + rows] = matrix[i][j] = rankCopy[find(i)] + 1
        return matrix