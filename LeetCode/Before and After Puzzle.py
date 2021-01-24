class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        hashMap, result = defaultdict(set), set()
        for i, phrase in enumerate(phrases):
            parts = phrase.split(' ', 1)
            hashMap[parts[0]].add((phrase, i))
        for i, phrase in enumerate(phrases):
            parts = phrase.rsplit(' ', 1)
            if parts[-1] in hashMap:
                for p, j in hashMap[parts[-1]]:
                    if i != j:
                        result.add(' '.join(parts[:-1] + p.split()))
        return sorted(result)