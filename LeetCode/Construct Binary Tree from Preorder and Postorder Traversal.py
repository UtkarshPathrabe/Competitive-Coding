# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        postorderIndexMap = {}
        for index, val in enumerate(postorder):
            postorderIndexMap[val] = index
        preorderIndexMap = {}
        for index, val in enumerate(preorder):
            preorderIndexMap[val] = index

        def constructTree(preStart: int, preEnd: int, postStart: int, postEnd: int) -> Optional[TreeNode]:
            if preStart > preEnd or postStart > postEnd:
                return None
            leftStartValue = preorder[preStart + 1] if (preStart + 1) < n else None
            rightStartValue = postorder[postEnd - 1] if (postEnd - 1) >= 0 else None
            leftTreeNodeCount = max(preorderIndexMap[rightStartValue] - preStart - 1, 0) if rightStartValue else 0
            rightTreeNodeCount = max(postorderIndexMap[leftStartValue] - postStart + 1, 0) if leftStartValue else 0
            leftTree = constructTree(preStart + 1, preStart + leftTreeNodeCount, postStart, postStart + leftTreeNodeCount - 1)
            rightTree = constructTree(preStart + leftTreeNodeCount + 1, preEnd, postStart + leftTreeNodeCount, postEnd - 1)
            return TreeNode(preorder[preStart], leftTree, rightTree)
        
        return constructTree(0, n - 1, 0, n - 1)