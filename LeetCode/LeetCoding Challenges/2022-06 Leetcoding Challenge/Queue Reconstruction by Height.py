class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        for person in sorted(people, key = lambda x : (-x[0], x[1])):
            result.insert(person[1], person)
        return result