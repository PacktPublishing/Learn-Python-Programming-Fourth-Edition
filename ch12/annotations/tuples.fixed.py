# annotations/tuples.fixed.py

# Tuple `a` is assigned to a tuple of length 1,
# with a single string element.
a: tuple[str] = ("hello",)

# Tuple `b` is assigned to a tuple of length 2,
# with an integer and a string element.
b: tuple[int, str] = (1, "one")

# Type checker error: the annotation indicates a tuple of
# length 1, but the tuple has 3 elements.
c: tuple[float] = (3.14, 1.0, -1.0)  # Wrong!
