from threading import Lock

class DiningPhilosophers:
    def __init__(self):
        self.forks = [Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        # To avoid deadlock philosopher at even places would try to acquire right fork first, rest would try to acquire left fork first
        if philosopher % 2 == 0:
            leftForkIndex, rightForkIndex = (philosopher + 1) % 5, (philosopher) % 5 
        else:
            leftForkIndex, rightForkIndex = (philosopher) % 5, (philosopher + 1) % 5
        self.forks[leftForkIndex].acquire()
        self.forks[rightForkIndex].acquire()
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        self.forks[leftForkIndex].release()
        self.forks[rightForkIndex].release()