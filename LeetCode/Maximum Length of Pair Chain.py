class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x : (x[1], x[0]))
        result, currentPairEnd = 1, pairs[0][1]
        for pair in pairs[1:]:
            if currentPairEnd < pair[0]:
                result, currentPairEnd = result + 1, pair[1]
        return result