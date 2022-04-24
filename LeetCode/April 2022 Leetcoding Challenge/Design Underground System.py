class UndergroundSystem:

    def __init__(self):
        self.checkInData, self.journeyData = {}, defaultdict(lambda : [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInData[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkInData.pop(id)
        self.journeyData[(startStation, stationName)][0] += (t - startTime)
        self.journeyData[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, totalTrips = self.journeyData[(startStation, endStation)]
        return totalTime / totalTrips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)