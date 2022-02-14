class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        freqMap, result = defaultdict(int), 0
        for t in time:
            if t % 60 == 0:
                result += freqMap[0]
            else:
                result += freqMap[60 - (t % 60)]
            freqMap[t % 60] += 1
        return result