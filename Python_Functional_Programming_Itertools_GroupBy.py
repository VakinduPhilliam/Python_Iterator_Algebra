# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# itertools.groupby(iterable, key=None)
# The operation of groupby() is similar to the uniq filter in Unix. 
# It generates a break or new group every time the value of the key function changes 
# (which is why it is usually necessary to have sorted the data using the same key function). 
# That behavior differs from SQL’s GROUP BY which aggregates common elements regardless 
# of their input order.

groups = []
uniquekeys = []
data = sorted(data, key=keyfunc)

for k, g in groupby(data, keyfunc):

    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)
