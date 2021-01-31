from threading import Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.executeZero = Lock()
        self.executeOdd = Lock()
        self.executeEven = Lock()
        self.executeOdd.acquire()
        self.executeEven.acquire()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.executeZero.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.executeOdd.release()
            else:
                self.executeEven.release()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.executeEven.acquire()
            printNumber(i)
            self.executeZero.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.executeOdd.acquire()
            printNumber(i)
            self.executeZero.release()