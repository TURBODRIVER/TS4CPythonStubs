# Annotations Created by TURBODRIVER

"""
Sims4 Collections Module.
"""

from typing import *

class frozendict(dict):
    """
    A frozen dictionary after the style of frozenset.  frozendict() can be constructed with multiple mappings.
    """

    def __init__(self, *args, **kwargs):
        """
        A frozen dictionary after the style of frozenset.  frozendict() can be constructed with multiple mappings.
        """

    def __add__(self, value: 'Mapping[Any, Any]') -> 'frozendict':
        """
        Return self+value.
        """

    def __contains__(self, key: 'Any') -> 'bool':
        """
        True if the dictionary has the specified key, else False.
        """

    def __delitem__(self, key: 'Any'):
        """
        Delete self[key].
        """

    def __getitem__(self, key: 'Any') -> 'Any':
        """
        Return self[key].
        """

    def __iter__(self) -> 'Iterator[Any]':
        """
        Implement iter(self).
        """

    def __len__(self) -> 'int':
        """
        Return len(self).
        """

    def __radd__(self, value: 'Mapping[Any, Any]') -> 'frozendict':
        """
        Return value+self.
        """

    def __setitem__(self, key: 'Any', value: 'Any'):
        """
        Set self[key] to value.
        """

    def clear(self):
        """
        Override of dict function to prevent its usage in frozendict, will throw an attribute error if used
        """

    def copy(self) -> 'frozendict':
        """
        D.copy() -> a shallow copy of D
        """

    def fromkeys(self, cls, iterable: 'Iterable[Any]', value: 'Optional[Any]' = None) -> 'frozendict':
        """
        Create a new dictionary with keys from iterable and values set to value.
        """

    def get(self, key: 'Any', default: 'Optional[Any]' = None) -> 'Optional[Any]':
        """
        Return the value for key if key is in the dictionary, else default.
        """

    def items(self) -> 'ItemsView[Any, Any]':
        """
        D.items() -> a set-like object providing a view on D's items
        """

    def keys(self) -> 'KeysView[Any]':
        """
        D.keys() -> a set-like object providing a view on D's keys
        """

    def pop(self, key: 'Any', default: 'Optional[Any]' = None) -> 'Any':
        """
        Override of dict function to prevent its usage in frozendict, will throw an attribute error if used
        """

    def popitem(self) -> 'Tuple[Any, Any]':
        """
        Override of dict function to prevent its usage in frozendict, will throw an attribute error if used
        """

    def setdefault(self, key: 'Any', default: 'Optional[Any]' = None) -> 'Any':
        """
        Override of dict function to prevent its usage in frozendict, will throw an attribute error if used
        """

    def update(self, *args, **kwargs):
        """
        Override of dict function to prevent its usage in frozendict, will throw an attribute error if used
        """

    def values(self) -> 'ValuesView[Any]':
        """
        D.values() -> an object providing a view on D's values
        """


def dictionary_intersection_values_match(d1: 'dict', d2: 'dict') -> 'bool':
    """
    Tests if intersecting dictionary values match.
    """
