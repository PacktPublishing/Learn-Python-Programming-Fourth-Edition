# decorators/time.measure.deco1.py
from time import sleep, time


def f(sleep_time=0.1):
    sleep(sleep_time)


def measure(func):
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, "took:", time() - t)

    return wrapper


f = measure(f)  # decoration point

f(0.2)  # f took: 0.20128178596496582
f(sleep_time=0.3)  # f took: 0.30509519577026367
print(f.__name__)  # wrapper  <- ouch!
