class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        reqIndex = word.index(ch)
        return word[:reqIndex + 1][::-1] + word[reqIndex + 1:]