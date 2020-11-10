# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        uLevel = float('inf')
        
        def bfsHelper(root):
            nonlocal uLevel
            queue = deque([(root, 0)])
            while queue:
                node, currentDepth = queue.popleft()
                if node.val == u.val:
                    uLevel = currentDepth
                if uLevel < currentDepth:
                    return None
                if uLevel == currentDepth and node.val != u.val:
                    return node
                if node.left:
                    queue.append((node.left, currentDepth + 1))
                if node.right:
                    queue.append((node.right, currentDepth + 1))
            return None
                
        return bfsHelper(root)