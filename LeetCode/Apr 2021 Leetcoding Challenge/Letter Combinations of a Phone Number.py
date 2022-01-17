class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        DIGIT_LETTER_MAP = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        result = list()
        def backtrack(currentString = [], currentIndex = 0):
            if currentIndex == len(digits):
                result.append(''.join(currentString))
                return
            elif currentIndex > len(digits):
                return
            for char in DIGIT_LETTER_MAP[digits[currentIndex]]:
                currentString.append(char)
                backtrack(currentString, currentIndex + 1)
                currentString.pop()
        backtrack()
        return result