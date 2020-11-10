# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        tree1Count, tree2Count = defaultdict(int), defaultdict(int)
        def bfsTraverse(root, frequencyCount):
            queue = deque([root,])
            while queue:
                node = queue.popleft()
                if node.left is None and node.right is None:
                    frequencyCount[node.val] += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        bfsTraverse(root1, tree1Count)
        bfsTraverse(root2, tree2Count)
        return tree1Count == tree2Count