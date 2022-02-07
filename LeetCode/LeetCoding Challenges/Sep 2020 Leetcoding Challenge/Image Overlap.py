class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        dimension, overlaps = len(A), 0
        
        def shiftAndCount(xShift, yShift, M, R):
            count = 0
            for rRow, mRow in enumerate(range(xShift, dimension)):
                for rCol, mCol in enumerate(range(yShift, dimension)):
                    if M[mRow][mCol] == 1 and R[rRow][rCol] == 1:
                        count += 1
            return count
        
        for yShift in range(dimension):
            for xShift in range(dimension):
                overlaps = max(overlaps, shiftAndCount(xShift, yShift, A, B))
                overlaps = max(overlaps, shiftAndCount(xShift, yShift, B, A))
        return overlaps        