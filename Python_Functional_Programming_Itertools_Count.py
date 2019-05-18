# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# itertools.count(start=0, step=1) 
# Make an iterator that returns evenly spaced values starting with number start. 
# Often used as an argument to map() to generate consecutive data points. 
# Also, used with zip() to add sequence numbers. Roughly equivalent to:
 
def count(start=0, step=1):

    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...

    n = start

    while True:

        yield n
        n += step
