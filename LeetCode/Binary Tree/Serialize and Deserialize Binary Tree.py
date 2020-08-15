# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def recursiveSerialize(root, encodedString):
            if root is None:
                encodedString += 'None,'
            else:
                encodedString += str(root.val) + ','
                encodedString = recursiveSerialize(root.left, encodedString)
                encodedString = recursiveSerialize(root.right, encodedString)
            return encodedString
        return recursiveSerialize(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def recursiveDeserialize(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            root = TreeNode(l[0])
            l.pop(0)
            root.left = recursiveDeserialize(l)
            root.right = recursiveDeserialize(l)
            return root
        dataList = data.split(',')
        root = recursiveDeserialize(dataList)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))