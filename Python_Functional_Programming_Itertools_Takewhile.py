# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# itertools.takewhile(predicate, iterable) 
# Make an iterator that returns elements from the iterable as long as the predicate is true. 
# Roughly equivalent to:
 
def takewhile(predicate, iterable):

    # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4

    for x in iterable:

        if predicate(x):
            yield x

        else:
            break
