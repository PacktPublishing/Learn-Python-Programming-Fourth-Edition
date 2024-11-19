# decorators/time.measure.start.py
from time import sleep, time


def f():
    sleep(0.3)


def g():
    sleep(0.5)


t = time()
f()
print("f took:", time() - t)  # f took: 0.3028988838195801

t = time()
g()
print("g took:", time() - t)  # g took: 0.507941722869873
