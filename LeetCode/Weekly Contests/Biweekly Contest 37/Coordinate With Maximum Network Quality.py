class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        
        def getNetworkQuality(pointX, pointY):
            quality = 0
            for x, y, q in towers:
                distance = math.dist((x, y), (pointX, pointY))
                if distance <= radius:
                    quality += int(q / (1 + distance))
            return quality
        
        maxQuality, result = float('-inf'), [0, 0]
        for x in range(51):
            for y in range(51):
                quality = getNetworkQuality(x, y)
                if quality > maxQuality:
                    maxQuality = quality
                    result = [x, y]
        return result