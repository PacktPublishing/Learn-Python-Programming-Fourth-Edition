# profiling/triples.py
def calc_triples(mx):
    triples = []
    for a in range(1, mx + 1):
        for b in range(a, mx + 1):
            hypotenuse = calc_hypotenuse(a, b)
            if is_int(hypotenuse):
                triples.append((a, b, int(hypotenuse)))
    return triples


def calc_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5


def is_int(n):
    return n.is_integer()


triples = calc_triples(1000)

"""
$ python -m cProfile profiling/triples.py
         1502538 function calls in 0.393 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.393    0.393 {built-in method builtins.exec}
        1    0.000    0.000    0.393    0.393 triples.py:1(<module>)
        1    0.143    0.143    0.393    0.393 triples.py:1(calc_triples)
   500500    0.087    0.000    0.147    0.000 triples.py:15(is_int)
   500500    0.102    0.000    0.102    0.000 triples.py:11(calc_hypotenuse)
   500500    0.060    0.000    0.060    0.000 {method 'is_integer' of 'float' objects}
     1034    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
