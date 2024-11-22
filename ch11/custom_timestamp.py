# custom_timestamp.py
from time import sleep


def debug(*msg, timestamp=[None]):
    from time import time  # local import

    print(*msg)

    if timestamp[0] is None:
        timestamp[0] = time()  # 1
    else:
        now = time()
        print(f" Time elapsed: {now - timestamp[0]:.3f}s")
        timestamp[0] = now  # 2


debug("Entering buggy piece of code...")
sleep(0.3)
debug("First step done.")
sleep(0.5)
debug("Second step done.")


"""
$ python custom_timestamp.py
Entering buggy piece of code...
First step done.
 Time elapsed: 0.300s
Second step done.
 Time elapsed: 0.500s
"""
