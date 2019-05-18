# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# itertools.compress(data, selectors) 
# Make an iterator that filters elements from data returning only those that have a 
# corresponding element in selectors that evaluates to True. Stops when either the data 
# or selectors iterables has been exhausted. Roughly equivalent to:
 
def compress(data, selectors):

    # compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F

    return (d for d, s in zip(data, selectors) if s)
