# Python Functional Programming Modules / functools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# functools — Higher-order functions and operations on callable objects
# The functools module is for higher-order functions: functions that act on or return 
# other functions. 
# In general, any callable object can be treated as a function for the purposes of this 
# module.
# functools.reduce(function, iterable[, initializer]) 
# Apply function of two arguments cumulatively to the items of sequence, from left to right, 
# so as to reduce the sequence to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 
# calculates ((((1+2)+3)+4)+5). 
# The left argument, x, is the accumulated value and the right argument, y, is the update value 
# from the sequence. 
# If the optional initializer is present, it is placed before the items of the sequence in the 
# calculation, and serves as a default when the sequence is empty. 
# If initializer is not given and sequence contains only one item, the first item is 
# returned.
 
def reduce(function, iterable, initializer=None):
    it = iter(iterable)

    if initializer is None:
        value = next(it)

    else:

        value = initializer

    for element in it:
        value = function(value, element)

    return value
