class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = [word for word in text.split(' ') if word != '']
        totalWordsLength, textLength = sum(len(word) for word in words), len(text)
        spaces = textLength - totalWordsLength
        if len(words) > 1:
            betweenSpaces, endSpace = divmod(spaces, len(words) - 1)
            return (' ' * betweenSpaces).join(words) + ' ' * endSpace
        elif len(words) == 1:
            return words[0] + ' ' * spaces
        else:
            return ''