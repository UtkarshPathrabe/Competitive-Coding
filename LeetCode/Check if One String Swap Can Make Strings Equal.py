class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffCharMap = defaultdict(list)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffCharMap['s1'].append(s1[i])
                diffCharMap['s2'].append(s2[i])
        return len(diffCharMap['s1']) in [0, 2] and sorted(diffCharMap['s1']) == sorted(diffCharMap['s2'])