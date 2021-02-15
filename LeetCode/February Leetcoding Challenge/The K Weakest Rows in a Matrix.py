class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result, soldierFreq = [], []
        for index, row in enumerate(mat):
            soldierFreq.append((row.count(1), index))
        soldierFreq.sort()
        return [i for freq, i in soldierFreq[:k]]