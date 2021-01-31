from threading import Lock

class H2O:
    def __init__(self):
        self.executeHydrogen = Lock()
        self.executeOxygen = Lock()
        self.executeOxygen.acquire()
        self.hydrogenCount = 0

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.executeHydrogen.acquire()
        self.hydrogenCount += 1
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        if self.hydrogenCount == 2:
            self.hydrogenCount = 0
            self.executeOxygen.release()
        else:
            self.executeHydrogen.release()
        
    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.executeOxygen.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.executeHydrogen.release()