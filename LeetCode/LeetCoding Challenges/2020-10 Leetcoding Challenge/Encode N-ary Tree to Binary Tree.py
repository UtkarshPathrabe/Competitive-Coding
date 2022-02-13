"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if root is None:
            return None
        rootNode = TreeNode(root.val)
        numberOfChildren = len(root.children)
        if numberOfChildren > 0:
            rootNode.left = self.encode(root.children[0])
        currentNode = rootNode.left
        for i in range(1, numberOfChildren):
            currentNode.right = self.encode(root.children[i])
            currentNode = currentNode.right
        return rootNode
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, rootNode: TreeNode) -> 'Node':
        if rootNode is None:
            return None
        root = Node(rootNode.val, [])
        current = rootNode.left
        while current:
            root.children.append(self.decode(current))
            current = current.right
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))