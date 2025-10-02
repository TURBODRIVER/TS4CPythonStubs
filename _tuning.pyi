"""
Tuning System Interface
"""

from typing import *


class BinaryTuning():
    """
    Binary tuning class.
    
    Exposes packed XML nodes within a binary resource.
    Important note: Element and iterator sub-objects created from a BinaryTuning object are
    weakly linked. Destroying the base BinaryTuning object will orphan all outstanding element
    and iterator objects, causing them to throw errors if used.
    """

    def __init__(self, kwarg0: Any = None):
        pass

    @property
    def root(self):
        """
        Returns the root node of the packed XML document.
        """

    @root.setter
    def root(self, value):
        """
        Returns the root node of the packed XML document.
        """


class BinaryTuningElement():
    """
    Binary tuning packed XML element class.
    
    This is a partial reimplementation of the xml.etree.ElementTree interface on top of a packed XML system.
    """

    def __init__(self, *args):
        pass

    def __getitem__(self):
        """
        Return self[key].
        """

    def __iter__(self):
        """
        Implement iter(self).
        """

    def __len__(self):
        """
        Return len(self).
        """

    def get(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        Returns the value of the named attribute, or default if the attribute is absent.
        """

    def items(self):
        """
        Returns a dict of element attributes.
        
        Note that this is different than iteration, which returns child elements.
        """

    @property
    def tag(self):
        """
        Returns the name of the element.
        """

    @tag.setter
    def tag(self, value):
        """
        Returns the name of the element.
        """

    @property
    def text(self):
        """
        Returns the text immediately after the element's begin tag within the element, or None if there is no text.
        """

    @text.setter
    def text(self, value):
        """
        Returns the text immediately after the element's begin tag within the element, or None if there is no text.
        """


class BinaryTuningElementIterator():
    """
    Iterates over child elements.
    """

    def __init__(self, *args):
        pass

    def __iter__(self):
        """
        Implement iter(self).
        """

    def __next__(self):
        """
        Implement next(self).
        """


def is_binary_merged_tuning(arg0):
    """
    Check whether a resource is a binary merged tuning object.
    
    Returns true if the resource is encoded in binary tuning format, or false otherwise (assumedly XML).
    """
