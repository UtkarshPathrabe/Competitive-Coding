class Node:
    
    def __init__(self, start, end):
        self.start, self.end, self.left, self.right = start, end, None, None
    
    def insert(self, node):
        if node.start >= self.end:
            if self.right is None:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if self.left is None:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)