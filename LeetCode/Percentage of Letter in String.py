class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        freq = 0
        for char in s:
            if char == letter:
                freq += 1
        return math.floor((freq * 100) / len(s))