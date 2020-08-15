class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        group1 = [(char, len(list(group))) for char, group in itertools.groupby(name)]
        group2 = [(char, len(list(group))) for char, group in itertools.groupby(typed)]
        if len(group1) != len(group2):
            return False
        return all(char1 == char2 and len1 <= len2 for (char1, len1), (char2, len2) in zip(group1, group2))