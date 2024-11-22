from typing import Callable


def get_input(fname: str, func: Callable | None = None):
    """Return inputs.

    Input is optionally parsed by `func`. When it's the case of
    empty lines, `func` isn't applied, and an empty string is
    returned.
    """
    if func is None:
        func = lambda x: x
    with open(fname) as s:
        return [
            func(stripped) if (stripped := l.rstrip()) else ""
            for l in s
        ]
