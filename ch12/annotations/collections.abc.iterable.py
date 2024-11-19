# annotations/collections.abc.iterable.py

from collections.abc import Iterable, Callable


def process_items(items: Iterable) -> None:
    for item in items:
        print(item)


def process_callback(
    arg: str, callback: Callable[[str], str]
) -> str:
    return callback(arg)


def greeter(name: str) -> str:
    return f"Hello, {name}!"


def reverse(name: str) -> str:
    return name[::-1]


if __name__ == "__main__":
    print(process_callback("Alice", greeter))  # Hello, Alice!
    print(process_callback("Alice", reverse))  # ecilA
