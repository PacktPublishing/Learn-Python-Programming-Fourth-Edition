# annotations/any.py
from typing import Any


# Equivalent definitions of the square function
def square(n):
    return n**2


def square_annotated(n: Any) -> Any:
    return n**2


# Equivalent definitions of the reverse function
def reverse(items: list) -> list:
    return list(reversed(items))


def reverse_any(items: list[Any]) -> list[Any]:
    return list(reversed(items))


if __name__ == "__main__":
    print(square(5))  # 25
    print(square_annotated(5))  # 25
    print(reverse([1, 2, 3]))  # [3, 2, 1]
    print(reverse_any([1, 2, 3]))  # [3, 2, 1]
