# files/write_not_exists.py
with open("write_x.txt", "x") as fw:  # this succeeds
    fw.write("Writing line 1")


with open("write_x.txt", "x") as fw:  # this fails
    fw.write("Writing line 2")


"""
$ python write_not_exists.py
Traceback (most recent call last):
  File "write_not_exists.py", line 6, in <module>
    with open("write_x.txt", "x") as fw:  # this fails
         ^^^^^^^^^^^^^^^^^^^^^^^^
FileExistsError: [Errno 17] File exists: 'write_x.txt'
"""
