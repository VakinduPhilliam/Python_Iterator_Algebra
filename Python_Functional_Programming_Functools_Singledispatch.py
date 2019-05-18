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
# @functools.singledispatch 
# Transform a function into a single-dispatch generic function.
# To define a generic function, decorate it with the @singledispatch decorator. 
# Note that the dispatch happens on the type of the first argument, create your function
# accordingly:
 
    from functools import singledispatch
    @singledispatch
 
   def fun(arg, verbose=False):

        if verbose:

            print("Let me just say,", end=" ")

        print(arg)
