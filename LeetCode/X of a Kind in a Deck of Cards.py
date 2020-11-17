class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        counter = Counter(deck)
        from fractions import gcd
        X = min(counter.values())
        for val in counter.values():
            X = gcd(X, val)
        if X < 2:
            return False
        for card, freq in counter.items():
            if freq % X != 0:
                return False
        return True