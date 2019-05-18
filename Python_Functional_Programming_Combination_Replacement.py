# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# itertools.combinations_with_replacement(iterable, r) 
# Return r length subsequences of elements from the input iterable allowing individual 
# elements to be repeated more than once.
# Combinations are emitted in lexicographic sort order. So, if the input iterable is 
# sorted, the combination tuples will be produced in sorted order.
# Elements are treated as unique based on their position, not on their value. So if the 
# input elements are unique, the generated combinations will also be unique.
# Roughly equivalent to:

def combinations_with_replacement(iterable, r):

    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC

    pool = tuple(iterable)
    n = len(pool)

    if not n and r:
        return
    indices = [0] * r

    yield tuple(pool[i] for i in indices)

    while True:

        for i in reversed(range(r)):

            if indices[i] != n - 1:
                break
        else:
            return

        indices[i:] = [indices[i] + 1] * (r - i)

        yield tuple(pool[i] for i in indices)
