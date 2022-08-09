class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def convertToMinutes(time: str) -> int:
            parts = time.split(':')
            return int(parts[0]) * 60 + int(parts[1])
        difference, result = convertToMinutes(correct) - convertToMinutes(current), 0
        options = [60, 15, 5, 1]
        for option in options:
            if difference > 0:
                result += difference // option
                difference = difference % option
        return result