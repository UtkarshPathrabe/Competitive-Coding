# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        count = Counter()
        result = []
        
        def dfsEncode(node):
            if node is None:
                return '#'
            else:
                key = '{},{},{}'.format(node.val, dfsEncode(node.left), dfsEncode(node.right))
                count[key] += 1
                if count[key] == 2:
                    result.append(node)
                print(node.val, key, count)
                return key
        
        dfsEncode(root)
        return result