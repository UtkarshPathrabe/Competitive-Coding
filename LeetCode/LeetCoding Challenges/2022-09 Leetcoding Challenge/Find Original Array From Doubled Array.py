class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        freqMap = Counter(changed)
        if len(changed) % 2 != 0:
            return []
        result = []
        for num in changed:
            if freqMap[num] > 0:
                # 0 multiplication edge case
                if num == 0 and freqMap[num] < 2:
                    return []
                # double doesn't exist
                if (2 * num) not in freqMap or freqMap[2 * num] == 0:
                    return []
                freqMap[num] -= 1
                freqMap[2 * num] -= 1
                result.append(num)
        return result