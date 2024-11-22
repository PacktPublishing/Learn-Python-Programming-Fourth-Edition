# profiling/triples_v4.py
def calc_triples(mx):
    triples = []
    for a in range(1, mx + 1):
        for b in range(a, mx + 1):
            hypotenuse = (a * a + b * b) ** 0.5
            if hypotenuse.is_integer():
                triples.append((a, b, int(hypotenuse)))
    return triples


triples = calc_triples(1000)

"""
$ python -m cProfile profiling/triples_v4.py
         501538 function calls in 0.186 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.186    0.186 {built-in method builtins.exec}
        1    0.000    0.000    0.186    0.186 triples_v4.py:1(<module>)
        1    0.128    0.128    0.186    0.186 triples_v4.py:1(calc_triples)
   500500    0.058    0.000    0.058    0.000 {method 'is_integer' of 'float' objects}
     1034    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
