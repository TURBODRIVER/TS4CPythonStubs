"""
Sims4 hash utility module
"""

from typing import *

KEYNAMEMAPTYPE_END = 7
KEYNAMEMAPTYPE_OBJECTINSTANCES = 3
KEYNAMEMAPTYPE_RESOURCES = 1
KEYNAMEMAPTYPE_RESOURCESTRINGS = 2
KEYNAMEMAPTYPE_STRINGHASHES = 5
KEYNAMEMAPTYPE_SWARM = 4
KEYNAMEMAPTYPE_TUNINGINSTANCES = 6
KEYNAMEMAPTYPE_UNUSED = 0


def hash32(kwarg0: Any = None, kwarg1: Any = None):
    """
    Get the FNV32 hash of the provided string.
    """


def hash64(arg0):
    """
    Get the FNV64 hash of the provided string.
    """


def unhash64(kwarg0: Any = None, kwarg1: Any = None) -> "str":
    """
    instance:int64[, table_type:int32] -> str
    Get unhashed name for a given FNV64 hash.
    """
