# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTreesHelper(start, end):
            if start > end:
                return [None,]
            trees = []
            for i in range(start, end + 1):
                leftSubTree = generateTreesHelper(start, i - 1)
                rightSubTree = generateTreesHelper(i + 1, end)
                for l in leftSubTree:
                    for r in rightSubTree:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        trees.append(root)
            return trees
        return generateTreesHelper(1, n) if n else []