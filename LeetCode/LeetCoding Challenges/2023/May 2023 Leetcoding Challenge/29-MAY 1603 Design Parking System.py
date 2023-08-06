class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigSize, self.bigCount, self.mediumSize, self.mediumCount, self.smallSize, self.smallCount = big, 0, medium, 0, small, 0

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.bigCount < self.bigSize:
                self.bigCount += 1
                return True
            return False
        elif carType == 2:
            if self.mediumCount < self.mediumSize:
                self.mediumCount += 1
                return True
            return False
        elif carType == 3:
            if self.smallCount < self.smallSize:
                self.smallCount += 1
                return True
            return False
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)