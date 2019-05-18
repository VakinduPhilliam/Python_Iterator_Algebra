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
# Example of efficiently computing Fibonacci numbers using a cache to implement a dynamic 
# programming technique:
 
@lru_cache(maxsize=None)

def fib(n):

    if n < 2:
        return n

    return fib(n-1) + fib(n-2)

[fib(n) for n in range(16)]

fib.cache_info()
CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)
