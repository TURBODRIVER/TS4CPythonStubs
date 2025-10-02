"""
Resource System Interface
"""

from typing import *


class Key():
    """
    Resource Key class.
    
    Resource Keys are composed of type, instance, and group fields.
    If one of the fields isn't specified, it defaults to an zero.
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
        pass

    @property
    def group(self):
        pass

    @group.setter
    def group(self, value):
        pass

    @staticmethod
    def hash32(s: str, type: int, group: int) -> "Key":
        """
        Return a new Key instance whose instance is set to the 32-bit hash
        value of the given string.
        """

    @staticmethod
    def hash64(s: str, type: int, group: int) -> "Key":
        """
        Return a new Key instance whose instance is set to the 64-bit hash
        value of the given string.
        """

    @property
    def instance(self):
        pass

    @instance.setter
    def instance(self, value):
        pass

    @property
    def type(self):
        pass

    @type.setter
    def type(self, value):
        pass


LOT_LOAD_HITTING_THEIR_MARKS_BEGIN = 10012
LOT_LOAD_HITTING_THEIR_MARKS_END = 10013
LOT_LOAD_ON_ZONE_LOAD_BEGIN = 10004
LOT_LOAD_ON_ZONE_LOAD_END = 10005
LOT_LOAD_POSTURE_GRAPH_BEGIN = 10002
LOT_LOAD_POSTURE_GRAPH_END = 10003
LOT_LOAD_RESTORE_CAREER_BEGIN = 10010
LOT_LOAD_RESTORE_CAREER_END = 10011
LOT_LOAD_SIM_SPAWNER_BEGIN = 10008
LOT_LOAD_SIM_SPAWNER_END = 10009
LOT_LOAD_SITUATIONS_BEGIN = 10006
LOT_LOAD_SITUATIONS_END = 10007
LOT_LOAD_WAIT_FOR_SIM_SPAWNER_SERVICE_BEGIN = 10014
LOT_LOAD_WAIT_FOR_SIM_SPAWNER_SERVICE_END = 10015
LOT_LOAD_ZONE_SPIN_UP_BEGIN = 10000
LOT_LOAD_ZONE_SPIN_UP_END = 10001
RESMAN_API_VERSION = 2


class Resource():
    """
    Resource class.
    
    Resources are essentially bytes buffers with unique keys.
    """

    def __init__(self, *args):
        pass

    @property
    def key(self):
        """
        Resource key
        """

    @key.setter
    def key(self, value):
        """
        Resource key
        """


def databases() -> "tuple":
    """
    -> tuple
    
    Get the list of registered databases (path strings.
    """


def does_key_exist(key) -> "bool":
    """
    -> bool
    
    Return true if key exist in resource manager.
    """


def get_name_from_key(key) -> "string":
    """
    -> string
    
    Get the name of a resource for the given key.
    """


def get_normalized_key(key) -> "key":
    """
    -> key
    
    Return a Resource Key that accounts for modded content, i.e.
    a key that has its group's high bit set if its instance's high bit
    is also set, for certain resource types.
    """


def list(group=None, type=None) -> "list of resources":
    """
    -> list of resources
    
    Retrieve a list of available resources, using key as a filter.
    """


def list_local(key=None, include_packed=True, packed_types=None) -> "list of resources":
    """
    -> list of resources
    
    Retrieve a tuple of two lists of ResourceKey objects. The first contains keys
    of each file in LocalWork, if key available, otherwise keys modified after the
    passed in key. The second contains keys of all deleted resource.
    
    If include_packed is True, also include resources from packed package files. The
    optional packed_types list restricts the returned key list to the specified set
    of resource types (API v2+.
    """


def load(key) -> "resource":
    """
    -> resource
    
    Load a resource based on its key.
    """


def make_resource_hot_swappable(typeId):
    """
    Make resources with the given type id hot-swappable.
    """


def purge_cache():
    """
    Purge the ResourceMan resource cache.
    """


def python_telemetry_event(eventIndex):
    """
    Used to profile how long Python operations took and sends them to telemetry.
    """


def register_change_notification(callback, group=None, type=None) -> "handle":
    """
    -> handle
    
    Register/Unregister for the resource system to call the provided callback when resources matching the provided filters change.
    """


def register_pack_hotload_callback(bool, callback) -> "handle":
    """
    -> handle
    
    Register/Unregister for the resource system to call the provided callback when is ready to be hot loaded or unloaded.
    The callback should accept a bool for load (true, false for unload, and a list of tuples which are a (type, list of keys.
    """


def register_pack_hotload_request_callback(bool, callback) -> "handle":
    """
    -> handle
    
    Register/Unregister for the resource system to call the provided callback when a pack is requested to be hot loaded.
    The first parameter is true to register, false to unregister.
    The callback should accept a bool for load (true, false for unload, a pack id, and a list of types.
    """


def release_preload_buffers():
    """
    Tell the resource system to free the memory used by the preload buffer optimization.
    """


def unregister_change_notification(callback):
    """
    Unregiser for a resource system callback when the filtered files change.
    """
