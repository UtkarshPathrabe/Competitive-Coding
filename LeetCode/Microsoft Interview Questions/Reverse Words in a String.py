class Solution:
    def reverseWords(self, s: str) -> str:
        listOfWords = [word.strip() for word in s.strip().split(' ') if word != '']
        def helper(left, right):
            if left < right:
                listOfWords[left], listOfWords[right] = listOfWords[right], listOfWords[left]
                helper(left + 1, right -1)
        helper(0, len(listOfWords) - 1)
        return ' '.join(listOfWords)