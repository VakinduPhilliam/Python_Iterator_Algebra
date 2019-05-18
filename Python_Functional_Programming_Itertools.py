# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# itertools.accumulate(iterable[, func]) 
# Make an iterator that returns accumulated sums, or accumulated results of other binary 
# functions (specified via the optional func argument).

def accumulate(iterable, func=operator.add):
    'Return running totals'

    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120

    it = iter(iterable)

    try:
        total = next(it)

    except StopIteration:
        return
    yield total

    for element in it:
        total = func(total, element)
        yield total
