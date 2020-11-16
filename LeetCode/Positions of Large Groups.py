class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start, result = 0, []
        for char, group in itertools.groupby(s):
            group = list(group)
            if len(group) > 2:
                result.append([start, start + len(group) - 1])
            start += len(group)
        return result