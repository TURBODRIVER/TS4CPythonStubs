"""
Low-level Python utility functions.
"""

from typing import *


def change_gc_policy(arg0):
    """
    Set the python garbage collection policy.
    """


def set_function_closure(function, closure, remaps):
    """
    Set the __closure__ of function to value.
    
    function: the function object whose closure should be changed.
    closure: None or a tuple of cell objects, usually from the __closure__ 
        attribute of a function object.
    remaps: a dict containing replacements for members of the closure.
    
    "Not for the faint of heart."
    """


def try_highwater_gc() -> "bool":
    """
    -> bool
    
    If we've reached the highwater low trigger, this will run a level 2 GC.Return True if we did run GC. Return False if we did not.This should only be called at an opportune moment (i.e. during a modal dialog,while already at a loading screen, etc.
    """


class tupledescriptor():
    def __init__(self, arg0):
        pass

    def __get__(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        Return an attribute of instance, which is of type owner.
        """
