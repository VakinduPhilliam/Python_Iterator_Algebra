# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# itertools.product(*iterables, repeat=1) 
# Cartesian product of input iterables.
# Roughly equivalent to nested for-loops in a generator expression. For example, product(A, B) 
# returns the same as ((x,y) for x in A for y in B).
# The nested loops cycle like an odometer with the rightmost element advancing on every iteration. 
# This pattern creates a lexicographic ordering so that if the input’s iterables are sorted, the 
# product tuples are emitted in sorted order.
# To compute the product of an iterable with itself, specify the number of repetitions with the 
# optional repeat keyword argument. For example, product(A, repeat=4) means the same as 
# product(A, A, A, A).
# This function is roughly equivalent to the following code, except that the actual implementation 
# does not build up intermediate results in memory:

def product(*args, repeat=1):

    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111

    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]

    for pool in pools:
        result = [x+[y] for x in result for y in pool]

    for prod in result:
        yield tuple(prod)
