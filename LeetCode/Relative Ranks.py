class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scorePositionMap = {};
        for index, s in enumerate(score):
            scorePositionMap[s] = index
        newScore = sorted(score, reverse = True)
        result = ['' for _ in range(len(score))]
        for index, s in enumerate(newScore):
            if index == 0:
                result[scorePositionMap[s]] = 'Gold Medal'
            elif index == 1:
                result[scorePositionMap[s]] = 'Silver Medal'
            elif index == 2:
                result[scorePositionMap[s]] = 'Bronze Medal'
            else:
                result[scorePositionMap[s]] = str(index + 1)
        return result