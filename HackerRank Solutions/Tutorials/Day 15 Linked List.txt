class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next
    def insert(self,head,data):
        new_node = Node(data)
        if head:
            curr = head
            tail = None
            while curr:
                if tail == None:
                    tail = head
                else:
                    tail = tail.next
                curr = curr.next
            tail.next = new_node
            return head
        else:
            return new_node
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);