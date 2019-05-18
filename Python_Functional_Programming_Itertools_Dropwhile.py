# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# itertools.dropwhile(predicate, iterable) 
# Make an iterator that drops elements from the iterable as long as the predicate is true; 
# afterwards, returns every element. Note, the iterator does not produce any output until 
# the predicate first becomes false, so it may have a lengthy start-up time. 
# Roughly equivalent to:
 
def dropwhile(predicate, iterable):

    # dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1

    iterable = iter(iterable)

    for x in iterable:

        if not predicate(x):
            yield x
            break

    for x in iterable:
        yield x
