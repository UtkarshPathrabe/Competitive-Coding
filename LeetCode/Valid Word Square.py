class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        return words == [''.join(word) for word in zip_longest(*words, fillvalue='')]