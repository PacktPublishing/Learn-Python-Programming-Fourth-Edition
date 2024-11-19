# annotations/containers.py

# The type checker assumes all elements of the list are integers
a: list[int] = [1, 2, 3]

# We cannot specify two types for the elements of the list
# it only accepts a single type argument
b: list[int, str] = [1, 2, 3, "four"]  # Wrong!

# The type checker will infer that all keys in `c` are strings
# and all values are integers or strings
c: dict[str, int | str] = {"one": 1, "two": "2"}
