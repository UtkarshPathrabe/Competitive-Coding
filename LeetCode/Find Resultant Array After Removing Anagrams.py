class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result, index = [], 0
        while index < len(words):
            result.append(words[index])
            increment = 1
            map1 = Counter(words[index])
            while (index + increment) < len(words):
                map2 = Counter(words[index + increment])
                if map1 != map2:
                    break
                increment += 1
            index += increment
        return result