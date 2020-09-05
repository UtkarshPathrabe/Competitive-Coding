class Solution:
    def numWays(self, s: str) -> int:
        sLen, oneIndices, numberOfOnes, modulus = len(s), [], 0, 10 ** 9 + 7
        for i, c in enumerate(s):
            if c == '1':
                oneIndices.append(i)
                numberOfOnes += 1
        if numberOfOnes == 0:
            return ((sLen - 1) * (sLen - 2) // 2) % modulus
        if numberOfOnes % 3 != 0:
            return 0
        onesInEachSlice = numberOfOnes // 3
        return ((oneIndices[onesInEachSlice] - oneIndices[onesInEachSlice - 1]) * (oneIndices[2 * onesInEachSlice] - oneIndices[2 * onesInEachSlice - 1])) % modulus