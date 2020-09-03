class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def getHashKey(s):
            if len(s) == 0:
                return ('ZERO')
            elif len(s) == 1:
                return ('ONE')
            else:
                return tuple([(ord(s[i + 1]) - ord(s[i])) % 26 for i in range(len(s) - 1)])
        hashMap = defaultdict(list)
        for s in strings:
            hashMap[getHashKey(s)].append(s)
        return hashMap.values()