class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arrSorted = sorted(arr)
        result, rankMap, rank = [], {}, 1
        for index, num in enumerate(arrSorted):
            if num not in rankMap:
                rankMap[num] = rank
                rank += 1
        for num in arr:
            result.append(rankMap[num])
        return result