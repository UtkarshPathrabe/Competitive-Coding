class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hashMap = defaultdict(int)
        for item in items1:
            hashMap[item[0]] += item[1]
        for item in items2:
            hashMap[item[0]] += item[1]
        return [[key, hashMap[key]] for key in sorted(hashMap.keys())]