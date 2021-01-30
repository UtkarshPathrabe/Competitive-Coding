from threading import Lock

class Foo:
    def __init__(self):
        self.firstExecuted = Lock()
        self.secondExecuted = Lock()
        self.firstExecuted.acquire()
        self.secondExecuted.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstExecuted.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.firstExecuted:
            printSecond()
            self.secondExecuted.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.secondExecuted:
            printThird()