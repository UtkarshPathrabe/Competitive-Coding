class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        perfectWords, lowerWords, devowelWords = set(wordlist), {}, {}
        def replaceVowels(word):
            return ''.join('*' if char in 'aeiou' else char for char in word)
        for word in wordlist:
            lowerWord = word.lower()
            lowerWords.setdefault(lowerWord, word)
            devowelWords.setdefault(replaceVowels(lowerWord), word)
        def solve(query):
            if query in perfectWords:
                return query
            lowerQuery = query.lower()
            if lowerQuery in lowerWords:
                return lowerWords[lowerQuery]
            devowelQuery = replaceVowels(lowerQuery)
            if devowelQuery in devowelWords:
                return devowelWords[devowelQuery]
            return ''
        return map(solve, queries)