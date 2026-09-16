# Annotations Created by TURBODRIVER

"""
Sims4 hash utility module
"""

from typing import *

def hash32(s: 'str', initial_hash: 'Optional[int]' = None) -> 'int':
    """
    Get the FNV32 hash of the provided string.
    """


def hash64(s: 'str', initial_hash: 'Optional[int]' = None) -> 'int':
    """
    Get the FNV64 hash of the provided string.
    """


def unhash64(instance: 'int', table_type: 'Optional[int]' = None) -> 'str':
    """
    instance:int64[, table_type:int32] -> str
    Get unhashed name for a given FNV64 hash.
    """


KEYNAMEMAPTYPE_END = 7
KEYNAMEMAPTYPE_OBJECTINSTANCES = 3
KEYNAMEMAPTYPE_RESOURCES = 1
KEYNAMEMAPTYPE_RESOURCESTRINGS = 2
KEYNAMEMAPTYPE_STRINGHASHES = 5
KEYNAMEMAPTYPE_SWARM = 4
KEYNAMEMAPTYPE_TUNINGINSTANCES = 6
KEYNAMEMAPTYPE_UNUSED = 0
