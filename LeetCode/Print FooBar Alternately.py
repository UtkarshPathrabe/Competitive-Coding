from threading import Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooExecuted = Lock()
        self.fooExecuted.acquire()
        self.barExecuted = Lock()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.barExecuted.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.fooExecuted.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.fooExecuted.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.barExecuted.release()