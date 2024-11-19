# example.strongly.typed.py
a = 2
b = "2"
print(a + b)


"""
$ python ch12/example.strongly.typed.py
Traceback (most recent call last):
  File "ch12/example.strongly.typed.py", line 3, in <module>
    print(a + b)
          ~~^~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""
