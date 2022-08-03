class Node:
    def __init__(self, count: int, key: str):
        self.count = count
        self.next, self.prev = None, None
        self.words = set()
        self.words.add(key)

class AllOne:

    def __init__(self):
        self.hashMap = defaultdict(Node)
        self.head = Node(-1, "")
        self.tail = Node(-1, "")
        self.head.next, self.tail.prev = self.tail, self.head
    
    def _addNode(self, prevNode: Node, newNode: Node, nextNode: Node) -> None:
        prevNode.next, nextNode.prev, newNode.prev, newNode.next = newNode, newNode, prevNode, nextNode
    
    def _removeNode(self, node: Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def inc(self, key: str) -> None:
        if key not in self.hashMap:
            if self.head.next.count == 1:
                self.hashMap[key] = self.head.next
                self.head.next.words.add(key)
            else:
                newNode = Node(1, key)
                self._addNode(self.head, newNode, self.head.next)
                self.hashMap[key] = newNode
        else:
            node = self.hashMap[key]
            node.words.remove(key)
            if node.next.count == node.count + 1:
                node.next.words.add(key)
                self.hashMap[key] = node.next
            else:
                newNode = Node(node.count + 1, key)
                self._addNode(node, newNode, node.next)
                self.hashMap[key] = newNode
            if len(node.words) == 0:
                self._removeNode(node)

    def dec(self, key: str) -> None:
        node = self.hashMap[key]
        node.words.remove(key)
        if node.prev.count == node.count - 1:
            node.prev.words.add(key)
            self.hashMap[key] = node.prev
        elif node.count - 1 > 0:
            newNode = Node(node.count - 1, key)
            self._addNode(node.prev, newNode, node)
            self.hashMap[key] = newNode
        else:
            del self.hashMap[key]
        if len(node.words) == 0:
            self._removeNode(node)

    def getMaxKey(self) -> str:
        for word in self.tail.prev.words:
            return word

    def getMinKey(self) -> str:
        for word in self.head.next.words:
            return word


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()