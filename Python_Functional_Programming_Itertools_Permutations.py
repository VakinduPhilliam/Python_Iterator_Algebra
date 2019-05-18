# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# itertools.permutations(iterable, r=None) 
# Return successive r length permutations of elements in the iterable.
# If r is not specified or is None, then r defaults to the length of the iterable and 
# all possible full-length permutations are generated.
# Permutations are emitted in lexicographic sort order. So, if the input iterable is 
# sorted, the permutation tuples will be produced in sorted order.
# Elements are treated as unique based on their position, not on their value. So if the 
# input elements are unique, there will be no repeat values in each permutation.

def permutations(iterable, r=None):
 
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210

    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r

    if r > n:
        return

    indices = list(range(n))
    cycles = list(range(n, n-r, -1))

    yield tuple(pool[i] for i in indices[:r])

    while n:

        for i in reversed(range(r)):
            cycles[i] -= 1

            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i

            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break

        else:
            return
