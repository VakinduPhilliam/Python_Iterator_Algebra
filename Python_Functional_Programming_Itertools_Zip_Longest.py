# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# itertools.zip_longest(*iterables, fillvalue=None) 
# Make an iterator that aggregates elements from each of the iterables. If the iterables 
# are of uneven length, missing values are filled-in with fillvalue. 
# Iteration continues until the longest iterable is exhausted. Roughly equivalent to:
 
def zip_longest(*args, fillvalue=None):

    # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-

    iterators = [iter(it) for it in args]
    num_active = len(iterators)

    if not num_active:
        return

    while True:
        values = []

        for i, it in enumerate(iterators):

            try:
                value = next(it)

            except StopIteration:
                num_active -= 1

                if not num_active:
                    return

                iterators[i] = repeat(fillvalue)
                value = fillvalue
            values.append(value)

        yield tuple(values)
