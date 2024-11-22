# annotations/basic.py


def greeter(name):
    return f"Hello, {name}!"


def greeter_annotated(name: str) -> str:
    return f"Hello, {name}!"


def greeter_annotated_age(name: str, age: int) -> str:
    return f"Hello, {name}! You are {age} years old."


if __name__ == "__main__":
    print(greeter("Alice"))
    print(greeter_annotated("Bob"))
    print(greeter_annotated_age("Charlie", 30))
