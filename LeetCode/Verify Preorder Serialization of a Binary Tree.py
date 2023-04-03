class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        slots = 1
        for node in nodes:
            if slots <= 0:
                return False
            slots += -1 if node == '#' else 1
        return slots == 0