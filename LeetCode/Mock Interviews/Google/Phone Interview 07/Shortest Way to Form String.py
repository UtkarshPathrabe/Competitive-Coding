class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        hashMap = defaultdict(list)
        for index, ch in enumerate(source):
            hashMap[ch].append(index)
        i, j, count = -1, 0, 1
        targetLength = len(target)
        while j < targetLength:
            if target[j] not in hashMap:
                return -1
            index = bisect.bisect(hashMap[target[j]], i)
            if index == len(hashMap[target[j]]):
                i = -1
                count += 1
            else:
                i = hashMap[target[j]][index]
                j += 1
        return count