class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        result = i = 0
        counter = defaultdict(int)
        for j, x in enumerate(tree):
            counter[x] += 1
            while len(counter) > 2:
                counter[tree[i]] -= 1
                if counter[tree[i]] == 0:
                    del counter[tree[i]]
                i += 1
            result = max(result, j - i + 1)
        return result