# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# itertools.filterfalse(predicate, iterable). 
# Make an iterator that filters elements from iterable returning only those for which the 
# predicate is False. 
# If predicate is None, return the items that are false. 
# Roughly equivalent to:
 
def filterfalse(predicate, iterable):

    # filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8

    if predicate is None:
        predicate = bool

    for x in iterable:

        if not predicate(x):
            yield x
