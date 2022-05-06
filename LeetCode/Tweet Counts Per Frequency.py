class TweetCounts:

    def __init__(self):
        self.recordsMap = defaultdict(list)
        self.recordsSortedMap = defaultdict(bool)
        self.freqMap = {
            "minute": 60,
            "hour": 3600,
            "day": 86400
        }

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.recordsMap[tweetName].append(time)
        self.recordsSortedMap[tweetName] = False

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta, tweetTimes, isTweetTimesSorted, start, result = self.freqMap[freq], self.recordsMap[tweetName], self.recordsSortedMap[tweetName], startTime, []
        if not isTweetTimesSorted:
            tweetTimes = sorted(tweetTimes)
            self.recordsMap[tweetName] = tweetTimes
            self.recordsSortedMap[tweetName] = True
        while start <= endTime:
            end = min(start + delta, endTime + 1)
            result.append(bisect.bisect_left(tweetTimes, end) - bisect.bisect_left(tweetTimes, start))
            start += delta
        return result

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)