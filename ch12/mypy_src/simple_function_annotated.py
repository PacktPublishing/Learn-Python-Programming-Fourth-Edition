# mypy_src/simple_function_annotated.py


def hypothenuse(a: float, b: float) -> float:
    return (a**2 + b**2) ** 0.5


print(hypothenuse(3, 4))  # This is fine
print(hypothenuse(3.5, 4.9))  # This is also fine
print(hypothenuse(complex(1, 2), 10))  # Type checker error
