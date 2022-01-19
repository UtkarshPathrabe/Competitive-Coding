from datetime import datetime
class Solution:
    def dayOfYear(self, date: str) -> int:
        return datetime(int(date[0:4]), int(date[5:7]), int(date[8:])).timetuple().tm_yday