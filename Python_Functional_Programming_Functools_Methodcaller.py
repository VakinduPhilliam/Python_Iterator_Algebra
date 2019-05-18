# Python Functional Programming Modules / functools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# operator — Standard operators as functions.
# The operator module exports a set of efficient functions corresponding to the intrinsic
# operators of Python.
# operator.methodcaller(name[, args...]) 
# Return a callable object that calls the method name on its operand. If additional arguments 
# and/or keyword arguments are given, they will be given to the method as well. For example:
# After f = methodcaller('name'), the call f(b) returns b.name().
# After f = methodcaller('name', 'foo', bar=1), the call f(b) returns b.name('foo', bar=1).
 
def methodcaller(name, *args, **kwargs):

    def caller(obj):
        return getattr(obj, name)(*args, **kwargs)

    return caller
