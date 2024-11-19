# annotations/tuples.any.length.py
from typing import Any

# We use the ellipsis to indicate that the tuple can have any
# number of elements.
a: tuple[int, ...] = (1, 2, 3)

# All the following are valid, because the tuple can have any
# number of elements.
a = ()
a = (7,)
a = (7, 8, 9, 10, 11)

# But this is an error, because the tuple can only have integers
a = ("hello", "world")

# We can specify a tuple that must be empty
b: tuple[()] = ()

# Finally, if we annotate a tuple like this:
c: tuple = (1, 2, 3)
# The type checker will treat it as if we had written:
c: tuple[Any, ...] = (1, 2, 3)
# And because of that, all the below are valid:
c = ()
c = ("hello", "my", "friend")
