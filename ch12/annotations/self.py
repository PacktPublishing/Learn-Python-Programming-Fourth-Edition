# annotations/self.py
from typing import Self
from collections.abc import Iterable
from dataclasses import dataclass


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def magnitude(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    @classmethod
    def sum_points(cls, points: Iterable[Self]) -> Self:
        return cls(
            sum(p.x for p in points),
            sum(p.y for p in points),
            sum(p.z for p in points),
        )


if __name__ == "__main__":
    p1 = Point(1, 2, 3)
    p2 = Point(4, 5, 6)
    print(Point.sum_points([p1, p2]))  # Point(x=5, y=7, z=9)
