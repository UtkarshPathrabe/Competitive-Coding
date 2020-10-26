class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        charMap, letters, maxFrogs = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}, [0] * 5, float('-inf')
        for letter in croakOfFrogs:
            charIndex = charMap[letter]
            if charIndex != 0 and letters[charIndex - 1] == 0:
                return -1
            letters[charIndex] += 1
            maxFrogs = max(maxFrogs, letters[charIndex])
            if charIndex == 4:
                for index in range(5):
                    letters[index] -= 1
        for index in range(5):
            if letters[index] != 0:
                return -1
        return maxFrogs