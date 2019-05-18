# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# itertools.combinations(iterable, r) 
# Return r length subsequences of elements from the input iterable.
# Combinations are emitted in lexicographic sort order. So, if the input iterable is 
# sorted, the combination tuples will be produced in sorted order.
# Elements are treated as unique based on their position, not on their value. So if the 
# input elements are unique, there will be no repeat values in each combination
# Roughly equivalent to:
 
def combinations(iterable, r):

    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123

    pool = tuple(iterable)
    n = len(pool)

    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)

    while True:

        for i in reversed(range(r)):

            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1

        for j in range(i+1, r):

            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
