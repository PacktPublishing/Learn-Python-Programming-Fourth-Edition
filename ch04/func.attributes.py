# func.attributes.py
def multiplication(a, b=1):
    """Return a multiplied by b."""
    return a * b


if __name__ == "__main__":

    special_attributes = [
        "__doc__",
        "__name__",
        "__qualname__",
        "__module__",
        "__defaults__",
        "__code__",
        "__globals__",
        "__dict__",
        "__closure__",
        "__annotations__",
        "__kwdefaults__",
    ]

    for attribute in special_attributes:
        print(attribute, "->", getattr(multiplication, attribute))

"""
__doc__ -> Return a multiplied by b.
__name__ -> multiplication
__qualname__ -> multiplication
__module__ -> __main__
__defaults__ -> (1,)
__code__ -> <code object multiplication at 0x104e65fe0, file "/Users/fab/code/lpp4ed/ch04/func.attributes.py", line 2>
__globals__ -> {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x104dfdc70>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/fab/code/lpp4ed/ch04/func.attributes.py', '__cached__': None, 'multiplication': <function multiplication at 0x104e96d40>, 'special_attributes': ['__doc__', '__name__', '__qualname__', '__module__', '__defaults__', '__code__', '__globals__', '__dict__', '__closure__', '__annotations__', '__kwdefaults__'], 'attribute': '__globals__'}
__dict__ -> {}
__closure__ -> None
__annotations__ -> {}
__kwdefaults__ -> None
"""
