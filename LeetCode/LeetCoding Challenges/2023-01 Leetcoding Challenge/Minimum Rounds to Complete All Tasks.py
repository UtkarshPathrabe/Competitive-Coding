class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freqMap = Counter(tasks)
        result = 0
        for freq in freqMap.values():
            if freq == 1:
                return -1
            elif freq % 3 == 0:
                result += freq // 3
            else:
                # If freq % 3 = 1; (freq / 3 - 1) groups of triplets and 2 pairs.
                # If freq % 3 = 2; (freq / 3) groups of triplets and 1 pair.
                result += (freq // 3) + 1
        return result