# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        result = []
        def removeNodes(node, toDelete, parentExists = False):
            nonlocal result
            if node is None:
                return None
            if node.val in toDelete:
                node.left = removeNodes(node.left, toDelete)
                node.right = removeNodes(node.right, toDelete)
                return None
            else:
                if not parentExists:
                    result.append(node)
                node.left = removeNodes(node.left, toDelete, True)
                node.right = removeNodes(node.right, toDelete, True)
                return node
        removeNodes(root, to_delete)
        return result