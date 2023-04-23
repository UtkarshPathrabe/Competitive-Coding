class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) == 0 or (r * c != len(mat) * len(mat[0])):
            return mat
        result, count = [[0] * c for _ in range(r)], 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                result[count // c][count % c], count = mat[i][j], count + 1
        return result