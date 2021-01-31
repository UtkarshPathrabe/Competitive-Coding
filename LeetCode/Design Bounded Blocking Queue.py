from threading import Semaphore

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.emptySlots = Semaphore(capacity)
        self.occupiedSlots = Semaphore(0)
        self.queue = deque()

    def enqueue(self, element: int) -> None:
        self.emptySlots.acquire()
        self.queue.append(element)
        self.occupiedSlots.release()

    def dequeue(self) -> int:
        self.occupiedSlots.acquire()
        element = self.queue.popleft()
        self.emptySlots.release()
        return element

    def size(self) -> int:
        return len(self.queue)