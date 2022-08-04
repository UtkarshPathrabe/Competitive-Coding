# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)
        def postorder(node: Optional[TreeNode]) -> int:
            if node:
                left = postorder(node.left)
                right = postorder(node.right)
                result = left + right + node.val
                freq[result] += 1
                return result
            return 0
        postorder(root)
        maxFreq = max(freq.values())
        return [x[0] for x in freq.items() if x[1] == maxFreq]