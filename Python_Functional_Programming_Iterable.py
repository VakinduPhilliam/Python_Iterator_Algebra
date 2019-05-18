# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# classmethod chain.from_iterable(iterable). 
# Alternate constructor for chain(). Gets chained inputs from a single iterable argument 
# that is evaluated lazily. Roughly equivalent to:
 
def from_iterable(iterables):

    # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F

    for it in iterables:

        for element in it:
            yield element
