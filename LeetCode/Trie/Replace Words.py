class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        Trie = lambda : defaultdict(Trie)
        trie = Trie()
        END = True
        for word in dictionary:
            current = trie
            for char in word:
                current = current.setdefault(char, Trie())
            current[END] = word
        
        def replace(word):
            current = trie
            for char in word:
                if char not in current or END in current:
                    break
                current = current[char]
            return current.get(END, word)
        
        return ' '.join(map(replace, sentence.split(' ')))