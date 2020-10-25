class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        satisfiedChildren, childIndex, cookieIndex = 0, 0, 0
        while childIndex < len(g) and cookieIndex < len(s):
            if s[cookieIndex] >= g[childIndex]:
                satisfiedChildren += 1
                childIndex += 1
            cookieIndex += 1
        return satisfiedChildren