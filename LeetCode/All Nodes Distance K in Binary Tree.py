# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parentMap = defaultdict(TreeNode)
        def dfs(node: Optional[TreeNode], parent = None):
            if node:
                parentMap[node] = parent
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        queue = deque([(target, 0),])
        seen = { target }
        while queue:
            if queue[0][1] == k:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for neighbour in (node.left, node.right, parentMap[node]):
                if neighbour and neighbour not in seen:
                    seen.add(neighbour)
                    queue.append((neighbour, d + 1))
        return []