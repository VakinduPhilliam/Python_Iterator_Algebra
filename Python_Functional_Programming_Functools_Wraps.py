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
# @functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
# This is a convenience function for invoking update_wrapper() as a function decorator 
# when defining a wrapper function. 
# It is equivalent to partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated). 
 
from functools import wraps
    def my_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwds):
            print('Calling decorated function')
            return f(*args, **kwds)
        return wrapper
   
    @my_decorator
    def example():
        """Docstring"""
        print('Called example function')
   
    example()

# Displays 'Calling decorated function'
# Displays 'Called example function'

    example.__name__

# Displays 'example'

    example.__doc__

# Displays 'Docstring'
