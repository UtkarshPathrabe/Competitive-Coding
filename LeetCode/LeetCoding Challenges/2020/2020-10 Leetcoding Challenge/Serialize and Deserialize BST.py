# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def preorder(node):
            if node:
                yield str(node.val)
                yield from preorder(node.left)
                yield from preorder(node.right)
            else:
                yield 'None'
        return ','.join(list(preorder(root)))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        nodeVals = data.split(',')
        def helper():
            if nodeVals[0] == 'None':
                nodeVals.pop(0)
                return None
            root = TreeNode(int(nodeVals[0]))
            nodeVals.pop(0)
            root.left = helper()
            root.right = helper()
            return root
        return helper()
                    

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans