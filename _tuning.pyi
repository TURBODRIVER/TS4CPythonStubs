# Annotations Created by TURBODRIVER

"""
Tuning System Interface
"""

from typing import *

import _resourceman

class BinaryTuning():
    """
    Binary tuning class.
    
    Exposes packed XML nodes within a binary resource.
    Important note: Element and iterator sub-objects created from a BinaryTuning object are
    weakly linked. Destroying the base BinaryTuning object will orphan all outstanding element
    and iterator objects, causing them to throw errors if used.
    """

    def __init__(self, resource_key: '_resourceman.Key'):
        """
        Binary tuning class.
        
        Exposes packed XML nodes within a binary resource.
        Important note: Element and iterator sub-objects created from a BinaryTuning object are
        weakly linked. Destroying the base BinaryTuning object will orphan all outstanding element
        and iterator objects, causing them to throw errors if used.
        """

    @property
    def root(self) -> 'BinaryTuningElement':
        """
        Returns the root node of the packed XML document.
        """

    @root.setter
    def root(self, value: 'BinaryTuningElement'):
        """
        Returns the root node of the packed XML document.
        """


class BinaryTuningElement():
    """
    Binary tuning packed XML element class.
    
    This is a partial reimplementation of the xml.etree.ElementTree interface on top of a packed XML system.
    """

    def __init__(self):
        """
        Binary tuning packed XML element class.
        
        This is a partial reimplementation of the xml.etree.ElementTree interface on top of a packed XML system.
        """

    def __getitem__(self, index: 'Union[int, slice]') -> 'BinaryTuningElement':
        """
        Return self[key].
        """

    def __iter__(self) -> 'BinaryTuningElementIterator':
        """
        Implement iter(self).
        """

    def __len__(self) -> 'int':
        """
        Return len(self).
        """

    def get(self, key: 'str', default: 'Optional[Any]' = None) -> 'Optional[Any]':
        """
        Returns the value of the named attribute, or default if the attribute is absent.
        """

    def items(self) -> 'Dict[str, str]':
        """
        Returns a dict of element attributes.
        
        Note that this is different than iteration, which returns child elements.
        """

    @property
    def tag(self) -> 'str':
        """
        Returns the name of the element.
        """

    @tag.setter
    def tag(self, value: 'str'):
        """
        Returns the name of the element.
        """

    @property
    def text(self) -> 'Optional[str]':
        """
        Returns the text immediately after the element's begin tag within the element, or None if there is no text.
        """

    @text.setter
    def text(self, value: 'Optional[str]'):
        """
        Returns the text immediately after the element's begin tag within the element, or None if there is no text.
        """


class BinaryTuningElementIterator():
    """
    Iterates over child elements.
    """

    def __init__(self, element: 'BinaryTuningElement'):
        """
        Iterates over child elements.
        """

    def __iter__(self) -> 'BinaryTuningElementIterator':
        """
        Implement iter(self).
        """

    def __next__(self) -> 'BinaryTuningElement':
        """
        Implement next(self).
        """


def is_binary_merged_tuning(resource_key: '_resourceman.Key') -> 'bool':
    """
    Check whether a resource is a binary merged tuning object.
    
    Returns true if the resource is encoded in binary tuning format, or false otherwise (assumedly XML).
    """
