class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        result, count = 0, 0
        for box in boxTypes:
            result += min(truckSize - count, box[0]) * box[1]
            count += min(truckSize - count, box[0])
            if (count == truckSize):
                break
        return result