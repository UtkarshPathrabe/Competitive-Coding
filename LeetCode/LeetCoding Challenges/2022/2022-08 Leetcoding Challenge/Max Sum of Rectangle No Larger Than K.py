from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def countRangeSum(nums, U):
            SList, ans = SortedList([0]), -float("inf")
            for s in accumulate(nums):
                idx = SList.bisect_left(s - U) 
                if idx < len(SList): ans = max(ans, s - SList[idx])        
                SList.add(s)
            return ans
        
        m, n, ans = len(matrix), len(matrix[0]), -float("inf")
        
        for i, j in product(range(1, m), range(n)):
            matrix[i][j] += matrix[i-1][j]
                
        matrix = [[0]*n] + matrix
        
        for r1, r2 in combinations(range(m + 1), 2):
            row = [j - i for i, j in zip(matrix[r1], matrix[r2])]
            ans = max(ans, countRangeSum(row, k))
            
        return ans