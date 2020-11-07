class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        indexMap, result = defaultdict(list), -1
        for i, c in enumerate(s):
            indexMap[c].append(i)
        for c, indices in indexMap.items():
            if len(indices) > 1:
                result = max(result, indices[-1] - indices[0] - 1)
        return result