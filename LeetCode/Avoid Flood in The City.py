class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        rainsLen = len(rains)
        lastRains, dryDayIndices = {}, []
        result = [-1] * rainsLen
        
        def getDryingDayForLake(day, lake):
            if len(dryDayIndices) == 0:
                return None
            else:
                for dryDayIndex in dryDayIndices:
                    if lastRains[lake] < dryDayIndex < day:
                        return dryDayIndex
                return None
        
        for day, lake in enumerate(rains):
            if lake > 0:
                if lake in lastRains:
                    dryingDay = getDryingDayForLake(day, lake)
                    if dryingDay is None:
                        return []
                    else:
                        result[dryingDay] = lake
                        dryDayIndices.remove(dryingDay)
                lastRains[lake] = day
            else:
                dryDayIndices.append(day)
        
        while dryDayIndices:
            result[dryDayIndices.pop()] = 1
        
        return result