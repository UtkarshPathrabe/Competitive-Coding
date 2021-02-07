# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        result, stack = [], []
        if root is None:
            return result
        def isLeaf(node):
            return node.left is None and node.right is None
        def addLeaves(node):
            if isLeaf(node):
                result.append(node.val)
            else:
                if node.left is not None:
                    addLeaves(node.left)
                if node.right is not None:
                    addLeaves(node.right)
        if not isLeaf(root):
            result.append(root.val)
        currentNode = root.left
        while currentNode:
            if not isLeaf(currentNode):
                result.append(currentNode.val)
            if currentNode.left is not None:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        addLeaves(root)
        currentNode = root.right
        while currentNode:
            if not isLeaf(currentNode):
                stack.append(currentNode.val)
            if currentNode.right is not None:
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left
        result.extend(stack[::-1])
        return result