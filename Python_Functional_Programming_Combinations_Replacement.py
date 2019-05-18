# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# The code for combinations_with_replacement() can be also expressed as a subsequence 
# of product() after filtering entries where the elements are not in sorted order 
# (according to their position in the input pool):
 
def combinations_with_replacement(iterable, r):

    pool = tuple(iterable)
    n = len(pool)

    for indices in product(range(n), repeat=r):

        if sorted(indices) == list(indices):

            yield tuple(pool[i] for i in indices)
