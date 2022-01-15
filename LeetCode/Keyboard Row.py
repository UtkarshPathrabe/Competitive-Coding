class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        def isValid(word: str) -> bool:
            hashSet = set()
            for char in word:
                if char in 'qwertyuiop':
                    hashSet.add(0)
                elif char in 'asdfghjkl':
                    hashSet.add(1)
                elif char in 'zxcvbnm':
                    hashSet.add(2)
            return len(hashSet) == 1
        for word in words:
            if isValid(word.lower()):
                result.append(word)
        return result