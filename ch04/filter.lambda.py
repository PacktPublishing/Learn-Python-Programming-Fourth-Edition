# filter.lambda.py
def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n)))


print(get_multiples_of_five(30))  # [0, 5, 10, 15, 20, 25]
