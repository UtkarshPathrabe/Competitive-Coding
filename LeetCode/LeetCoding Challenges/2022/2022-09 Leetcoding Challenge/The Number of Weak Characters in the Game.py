class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x : (-x[0], x[1]))
        maxDefense, result = 0, 0
        for attack, defense in properties:
            if defense < maxDefense:
                result += 1
            else:
                maxDefense = defense
        return result