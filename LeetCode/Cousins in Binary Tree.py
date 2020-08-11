# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = deque([root])
        while queue:
            siblings, cousins = False, False
            nodesAtThisDepth = len(queue)
            for _ in range(nodesAtThisDepth):
                node = queue.popleft()
                if node is None:
                    siblings = False
                else:
                    if node.val == x or node.val == y:
                        if not cousins:
                            cousins, siblings = True, True
                        else:
                            return not siblings
                    queue.append(node.left) if node.left else None
                    queue.append(node.right) if node.right else None
                    queue.append(None)
            if cousins:
                return False
        return False