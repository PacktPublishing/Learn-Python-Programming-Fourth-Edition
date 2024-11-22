# annotations/tuples.named.py

from typing import NamedTuple


class Person(NamedTuple):
    name: str
    age: int


fab = Person("Fab", 48)
print(fab)  # Person(name='Fab', age=48)
print(fab.name)  # Fab
print(fab.age)  # 48
print(fab[0])  # Fab
print(fab[1])  # 48


# The above is equivalent to:
# import collections
# Person = collections.namedtuple("Person", ["name", "age"])


class Point(NamedTuple):
    x: int
    y: int
    z: int = 0


p = Point(1, 2)
print(p)  # Point(x=1, y=2, z=0)
