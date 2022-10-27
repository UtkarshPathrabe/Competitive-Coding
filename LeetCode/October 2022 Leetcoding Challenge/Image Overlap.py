class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        dimension, overlaps = len(A), 0
        
        def shiftAndCount(xShift, yShift, M, R):
            leftShiftCount, rightShiftCount = 0, 0
            for rRow, mRow in enumerate(range(yShift, dimension)):
                for rCol, mCol in enumerate(range(xShift, dimension)):
                    if M[mRow][mCol] == 1 and M[mRow][mCol] == R[rRow][rCol]:
                        leftShiftCount += 1
                    if M[mRow][rCol] == 1 and M[mRow][rCol] == R[rRow][mCol]:
                        rightShiftCount += 1
            return max(leftShiftCount, rightShiftCount)
        
        for yShift in range(dimension):
            for xShift in range(dimension):
                overlaps = max(overlaps, shiftAndCount(xShift, yShift, A, B))
                overlaps = max(overlaps, shiftAndCount(xShift, yShift, B, A))
        return overlaps