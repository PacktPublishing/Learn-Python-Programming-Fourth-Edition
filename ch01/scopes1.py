# scopes1.py
# Local versus Global

# we define a function, called local
def local():
    age = 7
    print(age)

# we define age within the global scope
age = 5

# we call, or `execute` the function local
local()

print(age)
