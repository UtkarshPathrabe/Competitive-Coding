from threading import Lock

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.executeFizz = Lock()
        self.executeBuzz = Lock()
        self.executeFizzBuzz = Lock()
        self.executeNumber = Lock()
        self.executeFizz.acquire()
        self.executeBuzz.acquire()
        self.executeFizzBuzz.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
    	for i in range(3, self.n + 1, 3):
            if i % 5:
                self.executeFizz.acquire()
                printFizz()
                if (i + 1) % 5 == 0:
                    self.executeBuzz.release()
                else:
                    self.executeNumber.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	for i in range(5, self.n + 1, 5):
            if i % 3:
                self.executeBuzz.acquire()
                printBuzz()
                if (i + 1) % 3 == 0:
                    self.executeFizz.release()
                else:
                    self.executeNumber.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(15, self.n + 1, 15):
            self.executeFizzBuzz.acquire()
            printFizzBuzz()
            self.executeNumber.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 != 0:
                self.executeNumber.acquire()
                printNumber(i)
                if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                    self.executeFizzBuzz.release()
                elif (i + 1) % 3 == 0:
                    self.executeFizz.release()
                elif (i + 1) % 5 == 0:
                    self.executeBuzz.release()
                else:
                    self.executeNumber.release()