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
# class functools.partialmethod(func, *args, **keywords). 
# Return a new partialmethod descriptor which behaves like partial except that it is 
# designed to be used as a method definition rather than being directly callable.
# func must be a descriptor or a callable (objects which are both, like normal functions, 
# are handled as descriptors).

class Cell(object):

        def __init__(self):
            self._alive = False

        @property

        def alive(self):
            return self._alive

        def set_state(self, state):
            self._alive = bool(state)

        set_alive = partialmethod(set_state, True)
        set_dead = partialmethod(set_state, False)
   
    c = Cell()
    c.alive             # Return False

    c.set_alive()
    c.alive             # Return True

