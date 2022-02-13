class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        numberOfDominoes = len(A)
        def checkValidity(x):
            rotationA, rotationB = 0, 0
            for i in range(numberOfDominoes):
                if A[i] != x and B[i] != x:
                    return -1
                elif A[i] != x:
                    rotationA += 1
                elif B[i] != x:
                    rotationB += 1
            return min(rotationA, rotationB)
        rotations = checkValidity(A[0])
        if rotations != -1 or A[0] == B[0]:
            return rotations
        else:
            return checkValidity(B[0])