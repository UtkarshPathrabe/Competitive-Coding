# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        lonelyNodes = []
        def dfs(node):
            if node:
                if node.left is None and node.right is None:
                    return
                elif node.left is not None and node.right is not None:
                    dfs(node.left)
                    dfs(node.right)
                    return
                else:
                    if node.left:
                        lonelyNodes.append(node.left.val)
                        dfs(node.left)
                    if node.right:
                        lonelyNodes.append(node.right.val)
                        dfs(node.right)
                    return
        dfs(root)
        return lonelyNodes