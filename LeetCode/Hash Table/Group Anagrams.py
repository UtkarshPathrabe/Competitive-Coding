class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            mapKey = [0] * 26
            for c in s:
                mapKey[ord(c) - ord('a')] += 1
            result[tuple(mapKey)].append(s)
        return result.values()