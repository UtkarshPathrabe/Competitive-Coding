class Solution:
    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
        
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # 1. Union-Find
        self.parent = list(range(len(s)))
        for a, b in pairs:
            self.union(a, b)
        # 2. Group
        group = defaultdict(lambda : ([], []))
        for i, c in enumerate(s):
            parent = self.find(i)
            group[parent][0].append(i)
            group[parent][1].append(c)
        # 3. Sorting
        result = [''] * len(s)
        for ids, chars in group.values():
            ids.sort()
            chars.sort()
            for c, i in zip(chars, ids):
                result[i] = c
        return ''.join(result)