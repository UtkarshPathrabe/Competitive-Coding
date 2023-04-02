class Logger:

    def __init__(self):
        self.logMap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if self.logMap.get(message) == None:
            self.logMap[message] = timestamp
            return True
        else:
            previousTimestamp = self.logMap[message]
            if timestamp - previousTimestamp >= 10:
                self.logMap[message] = timestamp
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)