class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        numMap = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                numMap[i - j].append(mat[i][j])
        for diag in numMap.keys():
            numMap[diag].sort(reverse = True)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = numMap[i - j].pop()
        return mat