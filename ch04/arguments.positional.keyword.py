# arguments.positional.keyword.py
def func(a, b, c):
    print(a, b, c)

func(42, b=1, c=2)

func(b=1, c=2, 42)  # positional arg after keyword args

"""
$ python arguments.positional.keyword.py
  File "arguments.positional.keyword.py", line 7
    func(b=1, c=2, 42)  # positional arg after keyword args
                     ^
SyntaxError: positional argument follows keyword argument
"""
