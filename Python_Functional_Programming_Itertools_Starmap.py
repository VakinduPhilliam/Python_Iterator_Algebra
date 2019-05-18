# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# itertools.starmap(function, iterable) 
# Make an iterator that computes the function using arguments obtained from the iterable. 
# Used instead of map() when argument parameters are already grouped in tuples from a single 
# iterable (the data has been “pre-zipped”). 
# The difference between map() and starmap() parallels the distinction between function(a,b) 
# and function(*c). Roughly equivalent to:
 
def starmap(function, iterable):

    # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000

    for args in iterable:
        yield function(*args)
