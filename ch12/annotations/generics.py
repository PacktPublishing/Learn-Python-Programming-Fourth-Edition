# annotations/generics.py
from typing import TypeVar

U = TypeVar("U")


def last[T](items: list[T]) -> T | None:
    return items[-1] if items else None


def first(items: list[U]) -> U | None:
    return items[0] if items else None


if __name__ == "__main__":
    print(last([1, 2, 3]))  # 3
    print(last([]))  # None

    print(first([1, 2, 3]))  # 1
    print(first([]))  # None
