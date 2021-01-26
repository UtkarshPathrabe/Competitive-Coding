class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        hashMap, result = defaultdict(int), []
        for name in names:
            currentName = name
            while currentName in hashMap:
                hashMap[name] += 1
                currentName = name + '(' + str(hashMap[name]) + ')'
            result.append(currentName)
            hashMap[currentName] = 0
        return result