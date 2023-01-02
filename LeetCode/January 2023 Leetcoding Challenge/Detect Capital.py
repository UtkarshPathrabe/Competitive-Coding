class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or ((word[0].upper() + word[1:].lower()) == word)