class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width = math.floor(math.sqrt(area))
        while width:
            if area % width == 0:
                return [area // width, width]
            else:
                width -= 1