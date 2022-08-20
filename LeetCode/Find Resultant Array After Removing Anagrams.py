class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result, index = [], 0
        while index < len(words):
            result.append(words[index])
            sortedWord = sorted(words[index])
            increment = 1
            while (index + increment) < len(words):
                if sortedWord != sorted(words[index + increment]):
                    break
                increment += 1
            index += increment
        return result