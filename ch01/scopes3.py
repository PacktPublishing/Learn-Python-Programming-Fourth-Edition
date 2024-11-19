# scopes3.py
# Local, Enclosing and Global


def enclosing_func():
    age = 13

    def local():
        # age does not belong to the scope defined by the local
        # function so Python will keep looking into the next
        # enclosing scope. This time age is found in the enclosing
        # scope
        print(age, 'printing from the local scope')

    # calling the function local
    local()

age = 5
print(age, 'printing from the global scope')

enclosing_func()
