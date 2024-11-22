# decorators/time.measure.dry.py
from time import sleep, time


def f():
    sleep(0.3)


def g():
    sleep(0.5)


def measure(func):
    t = time()
    func()
    print(func.__name__, "took:", time() - t)


measure(f)  # f took: 0.3043971061706543
measure(g)  # g took: 0.5050859451293945
