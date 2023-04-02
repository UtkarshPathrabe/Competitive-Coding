class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(' ')
        result = []
        def isVowel(word):
            return word[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for index, word in enumerate(words):
            if isVowel(word):
                result.append(word + 'ma' + ('a' * (index + 1)))
            else:
                result.append(word[1:] + word[0] + 'ma' + ('a' * (index + 1)))
        return ' '.join(result)