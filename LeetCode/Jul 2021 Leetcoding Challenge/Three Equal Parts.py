class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        IMPOSSIBLE, S = [-1, -1], sum(A)
        if S % 3:
            return IMPOSSIBLE
        T = S // 3
        if T == 0:
            return [0, len(A) - 1]
        breaks, currentSum = [], 0
        for i, digit in enumerate(A):
            if digit:
                currentSum += digit
                if currentSum in {1, T + 1, 2 * T + 1}:
                    breaks.append(i)
                if currentSum in {T, 2 * T, 3 * T}:
                    breaks.append(i)
        i1, j1, i2, j2, i3, j3 = breaks
        # The array is in the form W [i1, j1] X [i2, j2] Y [i3, j3] Z where [i1, j1] is a block of 1s, etc.
        if not(A[i1 : j1 + 1] == A[i2 : j2 + 1] == A[i3 : j3 + 1]):
            return IMPOSSIBLE
        # x, y, z: the number of zeros after part 1, 2, 3
        x, y, z = i2 - j1 - 1, i3 - j2 - 1, len(A) - j3 - 1
        if x < z or y < z:
            return IMPOSSIBLE
        j1, j2 = j1 + z, j2 + z
        return [j1, j2 + 1]