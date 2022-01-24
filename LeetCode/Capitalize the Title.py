class Solution:
    def capitalizeTitle(self, title: str) -> str:
        def capitalize(word: str) -> str:
            if len(word) in [1, 2]:
                return word.lower()
            else:
                return word[0].upper() + word[1:].lower()
        return ' '.join([capitalize(word) for word in title.split()])