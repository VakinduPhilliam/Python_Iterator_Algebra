# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# The code for permutations() can be also expressed as a subsequence of product(), filtered 
# to exclude entries with repeated elements (those from the same position in the input 
# pool):
 
def permutations(iterable, r=None):

    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r

    for indices in product(range(n), repeat=r):

        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)
