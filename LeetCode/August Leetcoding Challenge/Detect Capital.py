class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.title() == word or word.upper() == word or word.lower() == word:
            return True
        return False