# io_examples/string_io.py
import io


stream = io.StringIO()
stream.write("Learning Python Programming.\n")
print("Become a Python ninja!", file=stream)

contents = stream.getvalue()
print(contents)

stream.close()


# better alternative, using a context manager
with io.StringIO() as stream:
    stream.write("Learning Python Programming.\n")
    print("Become a Python ninja!", file=stream)

    contents = stream.getvalue()
    print(contents)


"""
$ python string_io.py
Learning Python Programming.
Become a Python ninja!

Learning Python Programming.
Become a Python ninja!
"""
