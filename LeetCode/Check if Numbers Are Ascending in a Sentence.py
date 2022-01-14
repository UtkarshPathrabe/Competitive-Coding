class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        currentNumber = -1
        for word in s.split():
            if word.isnumeric():
                if int(word) <= currentNumber:
                    return False
                else:
                    currentNumber = int(word)
        return True