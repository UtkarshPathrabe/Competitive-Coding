class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        hashSet = {TO for FROM, TO in edges}
        return [i for i in range(n) if i not in hashSet]