class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        count = [1] * n
        ans = [0] * n
        def postorder(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    postorder(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]
        def preorder(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - (2 * count[child]) + n
                    preorder(child, node)
        postorder()
        preorder()
        return ans