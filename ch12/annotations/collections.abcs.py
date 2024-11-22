# annotations/collections.abcs.py

from collections.abc import Mapping, Sequence


def average_bad(v: list[float]) -> float:
    return sum(v) / len(v)


def average(v: Sequence[float]) -> float:
    return sum(v) / len(v)


def greet_user_bad(user: dict[str, str]) -> str:
    return f"Hello, {user['name']}!"


def greet_user(user: Mapping[str, str]) -> str:
    return f"Hello, {user['name']}!"


def add_defaults_bad(
    data: Mapping[str, str]
) -> Mapping[str, str]:
    defaults = {"host": "localhost", "port": "5432"}
    return {**defaults, **data}


def add_defaults(data: Mapping[str, str]) -> dict[str, str]:
    defaults = {"host": "localhost", "port": "5432"}
    return {**defaults, **data}


if __name__ == "__main__":
    print(average_bad([1.0, 2.0, 3.0]))  # 2.0
    print(average((1.0, 2.0, 3.0)))  # 2.0

    print(greet_user_bad({"name": "Alice"}))  # Hello, Alice!
    print(greet_user({"name": "Charlie"}))  # Hello, Charlie!

    # {'host': 'db.example.com', 'port': 5432}
    print(add_defaults({"host": "db.example.com"}))
    print(add_defaults_bad({"host": "db.example.com"}))
