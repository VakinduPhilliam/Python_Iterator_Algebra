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
# functools.partial(func, *args, **keywords) 
# Return a new partial object which when called will behave like func called with the 
# positional arguments args and keyword arguments keywords. If more arguments are supplied 
# to the call, they are appended to args. If additional keyword arguments are supplied, 
# they extend and override keywords. 
# Roughly equivalent to:
 
def partial(func, *args, **keywords):

    def newfunc(*fargs, **fkeywords):

        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*args, *fargs, **newkeywords)

    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc
