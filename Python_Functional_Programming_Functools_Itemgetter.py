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
# operator.itemgetter(item) operator.itemgetter(*items) 
# Return a callable object that fetches item from its operand using the operand’s __getitem__() method. 
# If multiple items are specified, returns a tuple of lookup values
# After f = itemgetter(2), the call f(r) returns r[2].
# After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3]).

def itemgetter(*items):

    if len(items) == 1:
        item = items[0]

        def g(obj):
            return obj[item]

    else:

        def g(obj):
            return tuple(obj[item] for item in items)

    return g
