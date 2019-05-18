# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# itertools.cycle(iterable) 
# Make an iterator returning elements from the iterable and saving a copy of each. 
# When the iterable is exhausted, return elements from the saved copy. 
# Repeats indefinitely. Roughly equivalent to:
 
def cycle(iterable):

    # cycle('ABCD') --> A B C D A B C D A B C D ...

    saved = []

    for element in iterable:

        yield element
        saved.append(element)

    while saved:

        for element in saved:
              yield element
