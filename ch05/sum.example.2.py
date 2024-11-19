# sum.example.2.py
# s = sum([n**2 for n in range(10**10)])  # this is killed
s = sum(n**2 for n in range(10**10))  # this succeeds

print(s)  # prints: 333333333283333333335000000000
