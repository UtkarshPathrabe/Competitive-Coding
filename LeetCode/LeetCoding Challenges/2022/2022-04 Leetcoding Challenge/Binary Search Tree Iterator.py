# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self._stack = deque()
        self._processInorderLeftSubtree(root)
        
    def _processInorderLeftSubtree(self, node):
        while node:
            self._stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        nextNode = self._stack.pop()
        if nextNode.right:
            self._processInorderLeftSubtree(nextNode.right)
        return nextNode.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self._stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()