class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def crossProduct(A: List[List[int]], B: List[List[int]], C: List[List[int]]):
            return ((B[0] - A[0]) * (C[1] - A[1])) - ((B[1] - A[1]) * (C[0] - A[0]))
        if len(trees) <= 3:
            return trees
        trees.sort()
        upperHullTrees = [trees[0], trees[1]]
        for tree in trees[2:]:
            while len(upperHullTrees) >= 2 and crossProduct(upperHullTrees[-2], upperHullTrees[-1], tree) > 0:
                upperHullTrees.pop()
            upperHullTrees.append(tree)
        lowerHullTrees = [trees[-1], trees[-2]]
        for tree in trees[-3::-1]:
            while len(lowerHullTrees) >= 2 and crossProduct(lowerHullTrees[-2], lowerHullTrees[-1], tree) > 0:
                lowerHullTrees.pop()
            lowerHullTrees.append(tree)
        return sorted(set(tuple(x) for x in upperHullTrees + lowerHullTrees))