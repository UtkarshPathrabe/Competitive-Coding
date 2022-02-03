# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodesList = []
        
        def BFS(root):
            queue = deque([(root, 0, 0)])
            while len(queue) != 0:
                node, row, column = queue.popleft()
                if node is not None:
                    nodesList.append([column, row, node.val])
                    queue.append((node.left, row+1, column-1))
                    queue.append((node.right, row+1, column+1))
        
        BFS(root)
        
        nodesList.sort()
        
        d = OrderedDict()
        for column, row, val in nodesList:
            if column in d:
                d[column].append(val)
            else:
                d[column] = [val]
        return d.values()