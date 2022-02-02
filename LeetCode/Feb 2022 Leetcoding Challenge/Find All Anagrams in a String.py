class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pFreqMap, sFreqMap = Counter(p), defaultdict(int)
        result = []
        for i in range(0, len(p)):
            sFreqMap[s[i]] += 1
        if pFreqMap == sFreqMap:
            result.append(0)
        for i in range(1, len(s) - len(p) + 1):
            sFreqMap[s[i - 1]] -= 1
            sFreqMap[s[i + len(p) - 1]] += 1
            if sFreqMap[s[i - 1]] == 0:
                del sFreqMap[s[i - 1]]
            if pFreqMap == sFreqMap:
                result.append(i)
        return result