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
# To enable registering lambdas and pre-existing functions, the register() attribute can 
# be used in a functional form:
 
 def nothing(arg, verbose=False):
        print("Nothing.")
  
    fun.register(type(None), nothing)
