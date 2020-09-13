class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        for (nameKey, nameList), (typedKey, typedList) in zip_longest(*[groupby(name), groupby(typed)], fillvalue=('', [])):
            if nameKey != typedKey or len(list(nameList)) > len(list(typedList)):
                return False
        return True