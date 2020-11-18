class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        wordFreq = Counter(re.sub('\W+', ' ', paragraph.lower()).split())
        banned = set(banned)
        for word, freq in sorted(wordFreq.items(), key = lambda x : x[1], reverse = True):
            if word not in banned:
                return word