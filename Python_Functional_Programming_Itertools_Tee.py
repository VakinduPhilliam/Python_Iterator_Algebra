# Python Functional Programming Modules / itertools.
# Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks inspired by constructs 
# from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# The module standardizes a core set of fast, memory efficient tools that are useful 
# by themselves or in combination. Together, they form an “iterator algebra” making 
# it possible to construct specialized tools succinctly and efficiently in pure Python.
# itertools.tee(iterable, n=2) 
# Return n independent iterators from a single iterable.
# The following Python code helps explain what tee does (although the actual implementation 
# is more complex and uses only a single underlying FIFO queue).
# Roughly equivalent to:
 
def tee(iterable, n=2):
    it = iter(iterable)
    deques = [collections.deque() for i in range(n)]

    def gen(mydeque):

        while True:

            if not mydeque:             # when the local deque is empty

                try:
                    newval = next(it)   # fetch a new value and

                except StopIteration:
                    return

                for d in deques:        # load it to all the deques
                    d.append(newval)
            yield mydeque.popleft()

    return tuple(gen(d) for d in deques)
