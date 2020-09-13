class Solution:
    def nextClosestTime(self, time: str) -> str:
        result = startTime = int(time[:2], 10) * 60 + int(time[3:], 10)
        elapsed = 24 * 60
        validDigits = {int(i) for i in time if i != ':'}
        for h1, h2, m1, m2 in product(validDigits, repeat = 4):
            hours, minutes = h1 * 10 + h2, m1 * 10 + m2
            if hours < 24 and minutes < 60:
                newTime = hours * 60 + minutes
                timeElapsed = (newTime - startTime) % (24 * 60)
                if 0 < timeElapsed < elapsed:
                    result = newTime
                    elapsed = timeElapsed
        answer = divmod(result, 60)
        return '{:02d}:{:02d}'.format(answer[0], answer[1])