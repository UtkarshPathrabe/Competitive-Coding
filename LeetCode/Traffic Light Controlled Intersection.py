from threading import Lock

class TrafficLight:
    def __init__(self):
        self.lock = Lock()
        self.greenLightOn = 1

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:
        self.lock.acquire()
        if self.greenLightOn == roadId:
            crossCar()
        else:
            turnGreen()
            self.greenLightOn = roadId
            crossCar()
        self.lock.release()