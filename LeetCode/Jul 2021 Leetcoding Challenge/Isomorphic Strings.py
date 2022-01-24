class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        characterMap = {}
        for i, c in enumerate(s):
            if c not in characterMap:
                if t[i] not in characterMap.values():
                    characterMap[c] = t[i]
                else:
                    return False
            else:
                if characterMap[c] != t[i]:
                    return False
        return True