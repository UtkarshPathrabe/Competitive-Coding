# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        dummyHead = PolyNode()
        current = dummyHead
        while poly1 or poly2:
            x1 = poly1.coefficient if poly1 is not None else 0
            y1 = poly1.power if poly1 is not None else 0
            x2 = poly2.coefficient if poly2 is not None else 0
            y2 = poly2.power if poly2 is not None else 0
            if y1 == y2:
                val = x1 + x2
                if val != 0:
                    current.next = PolyNode(x = val, y = y1)
                    current = current.next
                poly1 = poly1.next if poly1 is not None else None
                poly2 = poly2.next if poly2 is not None else None
            elif y1 > y2:
                val = x1
                if val != 0:
                    current.next = PolyNode(x = val, y = y1)
                    current = current.next
                poly1 = poly1.next if poly1 is not None else None
            else:
                val = x2
                if val != 0:
                    current.next = PolyNode(x = val, y = y2)
                    current = current.next
                poly2 = poly2.next if poly2 is not None else None
        return dummyHead.next