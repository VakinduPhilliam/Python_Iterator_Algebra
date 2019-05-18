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
# @functools.total_ordering 
# Given a class defining one or more rich comparison ordering methods, this class decorator 
# supplies the rest. This simplifies the effort involved in specifying all of the possible 
# rich comparison operations:
# The class must define one of __lt__(), __le__(), __gt__(), or __ge__(). 
# In addition, the class should supply an __eq__() method.
  
@total_ordering

class Student:

    def _is_valid_operand(self, other):
        return (hasattr(other, "lastname") and
                hasattr(other, "firstname"))

    def __eq__(self, other):

        if not self._is_valid_operand(other):
            return NotImplemented

        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))

    def __lt__(self, other):

        if not self._is_valid_operand(other):
            return NotImplemented

        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))
