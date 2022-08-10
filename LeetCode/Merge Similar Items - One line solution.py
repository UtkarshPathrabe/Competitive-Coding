class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        return list(sorted((Counter({item[0]: item[1] for item in items1}) + Counter({item[0]: item[1] for item in items2})).items()))