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
# The functools module defines the following functions:
# @functools.lru_cache(maxsize=128, typed=False) 
# Decorator to wrap a function with a memoizing callable that saves up to the maxsize 
# most recent calls. It can save time when an expensive or I/O bound function is periodically 
# called with the same arguments.

@lru_cache(maxsize=32)

def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num

    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()

    except urllib.error.HTTPError:
        return 'Not Found'

for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
        pep = get_pep(n)
        print(n, len(pep))

    get_pep.cache_info()
CacheInfo(hits=3, misses=8, maxsize=32, currsize=8)
