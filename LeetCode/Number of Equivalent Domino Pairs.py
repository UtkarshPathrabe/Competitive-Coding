class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hashMap, result = defaultdict(int), 0
        for domino in dominoes:
            hashMap[frozenset(domino)] += 1
        for value in hashMap.values():
            result += value * (value - 1) // 2
        return result