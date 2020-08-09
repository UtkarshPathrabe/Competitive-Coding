class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        self.totalSum = 0
        root = Node(nums[0] % 10)
        
        for num in nums[1:]:
            depth, position, val = num // 100, (num // 10) % 10, num % 10
            position -= 1
            currentNode = root
            for d in range(depth - 2, -1, -1):
                if position < 2 ** d:
                    currentNode.left = currentNode = currentNode.left or Node(val)
                else:
                    currentNode.right = currentNode = currentNode.right or Node(val)
                position %= 2 ** d
                
        def preOrderTraversal(node, currentSum):
            if node is not None:
                currentSum += node.val
                if node.left is None and node.right is None:
                    self.totalSum += currentSum
                else:
                    preOrderTraversal(node.left, currentSum)
                    preOrderTraversal(node.right, currentSum)
        
        preOrderTraversal(root, 0)
        return self.totalSum