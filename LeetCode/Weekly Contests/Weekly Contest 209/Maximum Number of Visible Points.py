class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        radiansArray, onPlayerPoints = [], 0
        for point in points:
            if point[0] == location[0] and point[1] == location[1]:
                onPlayerPoints += 1
            else:
                radiansArray.append(math.atan2(point[1] - location[1], point[0] - location[0]))
        radiansArray.sort()
        radiansArray = radiansArray + [i + (2 * math.pi) for i in radiansArray[:-1]]
        angle = angle * (math.pi / 180)
        left = result = 0
        for right in range(len(radiansArray)):
            while radiansArray[left] < radiansArray[right] - angle:
                left += 1
            result = max(result, right - left + 1)
        return result + onPlayerPoints