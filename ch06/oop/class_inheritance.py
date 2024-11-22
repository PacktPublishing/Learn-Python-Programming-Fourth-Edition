# oop/class_inheritance.py
class Engine:
    def start(self):
        pass

    def stop(self):
        pass


class ElectricEngine(Engine):  # Is-A Engine
    pass


class V8Engine(Engine):  # Is-A Engine
    pass


class Car:
    engine_cls = Engine

    def __init__(self):
        self.engine = self.engine_cls()  # Has-A Engine

    def start(self):
        print(
            f"Starting {self.engine.__class__.__name__} for "
            f"{self.__class__.__name__}... Wroom, wroom!"
        )
        self.engine.start()

    def stop(self):
        self.engine.stop()


class RaceCar(Car):  # Is-A Car
    engine_cls = V8Engine


class CityCar(Car):  # Is-A Car
    engine_cls = ElectricEngine


class F1Car(RaceCar):  # Is-A RaceCar and also Is-A Car
    pass  # engine_cls same as parent


car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()
cars = [car, racecar, citycar, f1car]

for car in cars:
    car.start()

"""
$ python class_inheritance.py
Starting Engine for Car... Wroom, wroom!
Starting V8Engine for RaceCar... Wroom, wroom!
Starting ElectricEngine for CityCar... Wroom, wroom!
Starting V8Engine for F1Car... Wroom, wroom!
"""
