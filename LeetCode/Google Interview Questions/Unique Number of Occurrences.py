class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countsMap = Counter(arr)
        return len(countsMap.keys()) == len(set(countsMap.values()))