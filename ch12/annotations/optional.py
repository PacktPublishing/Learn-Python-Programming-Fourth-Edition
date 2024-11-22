# annotations/optional.py
from typing import Optional


def greeter(name: str = "stranger") -> str:
    return f"Hello, {name}!"


def greeter_optional(name: Optional[str] = None) -> str:
    if name is not None:
        return f"Hello, {name}!"
    return "No-one to greet!"


def another_greeter(name: str | None = None) -> str:
    if name is not None:
        return f"Hello, {name}!"
    return "No-one to greet!"


if __name__ == "__main__":
    print(greeter())  # Hello, stranger!
    print(greeter("Alice"))  # Hello, Alice!

    print(greeter_optional())  # No-one to greet!
    print(greeter_optional("Bob"))  # Hello, Bob!

    print(another_greeter())  # No-one to greet!
    print(another_greeter("Charlie"))  # Hello, Charlie!
