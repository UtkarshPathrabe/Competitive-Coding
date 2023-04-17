class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        freqMap = defaultdict(int)
        for row in mat:
            for value in row:
                freqMap[value] += 1
        for key in sorted(freqMap):
            if freqMap[key] == len(mat):
                return key
        return -1