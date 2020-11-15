# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        result = 0
        def postOrder(node):
            nonlocal result, distance
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [1]
            leftSubtree = postOrder(node.left)
            rightSubtree = postOrder(node.right)
            for l in leftSubtree:
                for r in rightSubtree:
                    if l + r <= distance:
                        result += 1
            returnList = []
            for l in leftSubtree:
                returnList.append(l + 1)
            for r in rightSubtree:
                returnList.append(r + 1)
            return returnList
        postOrder(root)
        return result