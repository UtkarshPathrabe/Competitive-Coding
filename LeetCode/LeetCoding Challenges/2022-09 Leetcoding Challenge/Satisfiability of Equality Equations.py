class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        root = [i for i in range(26)]
        index = lambda x: ord(x) - ord('a')
        for x, s, _, y in equations:
            if s == '=':
                root[find(index(x))] = find(index(y))
        for x, s, _, y in equations:
            if s == '!' and find(index(x)) == find(index(y)):
                return False
        return True