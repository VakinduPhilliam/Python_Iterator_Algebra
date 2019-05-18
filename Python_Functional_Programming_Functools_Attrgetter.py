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
# operator.attrgetter(attr) operator.attrgetter(*attrs) 
# Return a callable object that fetches attr from its operand. If more than one attribute is 
# requested, returns a tuple of attributes. The attribute names can also contain dots.
# After f = attrgetter('name'), the call f(b) returns b.name.
# After f = attrgetter('name', 'date'), the call f(b) returns (b.name, b.date).
# After f = attrgetter('name.first', 'name.last'), the call f(b) returns (b.name.first, b.name.last).
 
def attrgetter(*items):

    if any(not isinstance(item, str) for item in items):
        raise TypeError('attribute name must be a string')

    if len(items) == 1:
        attr = items[0]
        def g(obj):
            return resolve_attr(obj, attr)
    else:
        def g(obj):
            return tuple(resolve_attr(obj, attr) for attr in items)
    return g

def resolve_attr(obj, attr):

    for name in attr.split("."):
        obj = getattr(obj, name)
    return obj
