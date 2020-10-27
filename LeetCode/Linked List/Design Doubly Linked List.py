class ListNode:
    
    def __init__(self, val = None, nextNode = None, prevNode = None):
        self.val = val
        self.next = nextNode
        self.prev = prevNode

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head, self.tail = ListNode(0), ListNode(0)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        if index + 1 < self.size - index:
            currentNode = self.head
            for _ in range(index + 1):
                currentNode = currentNode.next
            return currentNode.val
        else:
            currentNode = self.tail
            for _ in range(self.size - index):
                currentNode = currentNode.prev
            return currentNode.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        predecessor, successor = self.head, self.head.next
        self.size += 1
        newNode = ListNode(val)
        newNode.next = successor
        newNode.prev = predecessor
        predecessor.next = newNode
        successor.prev = newNode

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        predecessor, successor = self.tail.prev, self.tail
        self.size += 1
        newNode = ListNode(val)
        newNode.next = successor
        newNode.prev = predecessor
        predecessor.next = newNode
        successor.prev = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        if index < 0:
            index = 0
        if index < self.size - index:
            predecessor = self.head
            for _ in range(index):
                predecessor = predecessor.next
            successor = predecessor.next
        else:
            successor = self.tail
            for _ in range(self.size - index):
                successor = successor.prev
            predecessor = successor.prev
        self.size += 1
        newNode = ListNode(val)
        newNode.next = successor
        newNode.prev = predecessor
        predecessor.next = newNode
        successor.prev = newNode

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        if index < self.size - index:
            predecessor = self.head
            for _ in range(index):
                predecessor = predecessor.next
            successor = predecessor.next.next
        else:
            successor = self.tail
            for _ in range(self.size - index - 1):
                successor = successor.prev
            predecessor = successor.prev.prev
        self.size -= 1
        predecessor.next = successor
        successor.prev = predecessor

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)