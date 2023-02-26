class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.centerX = x_center
        self.centerY = y_center
        self.r = radius
    
    def randPoint(self) -> List[float]:
        #switch to polar coordinates
        phi = (2 * random.random() - 1) * pi
        r = (random.random() * (self.r) ** 2) ** 0.5
        res = [self.centerX + r*cos(phi), self.centerY + r*sin(phi)]
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()