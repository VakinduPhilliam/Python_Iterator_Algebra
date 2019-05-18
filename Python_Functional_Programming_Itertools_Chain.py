# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# itertools.chain(*iterables) 
# Make an iterator that returns elements from the first iterable until it is exhausted, 
# then proceeds to the next iterable, until all of the iterables are exhausted. 
# Used for treating consecutive sequences as a single sequence. Roughly equivalent to:
 
def chain(*iterables):

    # chain('ABC', 'DEF') --> A B C D E F

    for it in iterables:

        for element in it:
            yield element
