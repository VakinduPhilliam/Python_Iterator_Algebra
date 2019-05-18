# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# itertools.repeat(object[, times]) 
# Make an iterator that returns object over and over again. Runs indefinitely unless the 
# times argument is specified. Used as argument to map() for invariant parameters to the 
# called function. Also used with zip() to create an invariant part of a tuple record.

def repeat(object, times=None):

    # repeat(10, 3) --> 10 10 10

    if times is None:

        while True:
            yield object
    else:

        for i in range(times):
            yield object
