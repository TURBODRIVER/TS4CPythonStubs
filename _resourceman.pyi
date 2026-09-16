# Annotations Created by TURBODRIVER

"""
Resource System Interface
"""

from typing import *

import types

class Key():
    """
    Resource Key class.
    
    Resource Keys are composed of type, instance, and group fields.
    If one of the fields isn't specified, it defaults to an zero.
    """

    def __init__(self, type: 'int' = 0, instance: 'int' = 0, group: 'int' = 0):
        """
        Resource Key class.
        
        Resource Keys are composed of type, instance, and group fields.
        If one of the fields isn't specified, it defaults to an zero.
        """

    @property
    def group(self) -> 'int':
        pass

    @group.setter
    def group(self, value: 'int'):
        pass

    @staticmethod
    def hash32(self, s: 'str', type: 'int', group: 'int' = 0) -> 'Key':
        """
        hash32(s, type, group)
        
        Return a new Key instance whose instance is set to the 32-bit hash
        value of the given string.
        """

    @staticmethod
    def hash64(self, s: 'str', type: 'int', group: 'int' = 0) -> 'Key':
        """
        hash64(s, type, group)
        
        Return a new Key instance whose instance is set to the 64-bit hash
        value of the given string.
        """

    @property
    def instance(self) -> 'int':
        pass

    @instance.setter
    def instance(self, value: 'int'):
        pass

    @property
    def type(self) -> 'int':
        pass

    @type.setter
    def type(self, value: 'int'):
        pass


class Resource():
    """
    Resource class.
    
    Resources are essentially bytes buffers with unique keys.
    """

    def __init__(self):
        """
        Resource class.
        
        Resources are essentially bytes buffers with unique keys.
        """

    @property
    def key(self) -> 'Key':
        """
        Resource key
        """

    @key.setter
    def key(self, value):
        """
        Resource key
        """


def databases() -> 'tuple':
    """
    databases() -> tuple
    
    Get the list of registered databases (path strings).
    """


def does_key_exist(key: 'Key') -> 'bool':
    """
    resourceman_does_key_exist(key) -> bool
    
    Return true if key exist in resource manager.
    """


def get_name_from_key(key: 'Key') -> 'str':
    """
    get_name_from_key(key) -> string
    
    Get the name of a resource for the given key.
    """


def get_normalized_key(key: 'Key') -> 'Key':
    """
    get_normalized_key(key) -> key
    
    Return a Resource Key that accounts for modded content, i.e.
    a key that has its group's high bit set if its instance's high bit
    is also set, for certain resource types.
    """


def list(group: 'Optional[int]' = None, type: 'Optional[int]' = None) -> 'List[Key]':
    """
    list(group=None, type=None) -> list of resources
    
    Retrieve a list of available resources, using key as a filter.
    """


def list_local(key: 'Optional[Key]' = None, include_packed: 'bool' = True, packed_types: 'Optional[Sequence[int]]' = None) -> 'Tuple[List[Key], List[Key]]':
    """
    list_local(key=None, include_packed=True, packed_types=None) -> list of resources
    
    Retrieve a tuple of two lists of ResourceKey objects. The first contains keys
    of each file in LocalWork, if key available, otherwise keys modified after the
    passed in key. The second contains keys of all deleted resource.
    
    If include_packed is True, also include resources from packed package files. The
    optional packed_types list restricts the returned key list to the specified set
    of resource types (API v2+).
    """


def load(key: 'Key') -> 'Optional[bytes]':
    """
    load(key) -> resource
    
    Load a resource based on its key.
    """


def make_resource_hot_swappable(type_id: 'int'):
    """
    make_resource_hot_swappable(typeId) -> None
    
    Make resources with the given type id hot-swappable.
    """


def purge_cache():
    """
    Purge the ResourceMan resource cache.
    """


def python_telemetry_event(event_index: 'int'):
    """
    python_telemetry_event(eventIndex) -> None
    
    Used to profile how long Python operations took and sends them to telemetry.
    """


def register_change_notification(callback, group=None, type=None):
    """
    register_change_notification(callback, group=None, type=None) -> handle
    
    Register/Unregister for the resource system to call the provided callback when resources matching the provided filters change.
    """


def register_pack_hotload_callback(enable: 'bool', callback: 'Callable[[bool, List[int]], bool]') -> 'int':
    """
    resourceman_register_pack_hotload_callback(bool, callback) -> handle
    
    Register/Unregister for the resource system to call the provided callback when is ready to be hot loaded or unloaded.
    The callback should accept a bool for load (true), false for unload, and a list of tuples which are a (type, list of keys).
    """


def register_pack_hotload_request_callback(enable: 'bool', callback: 'Callable[[bool, List[int]], bool]') -> 'int':
    """
    resourceman_register_pack_hotload_request_callback(bool, callback) -> handle
    
    Register/Unregister for the resource system to call the provided callback when a pack is requested to be hot loaded.
    The first parameter is true to register, false to unregister.
    The callback should accept a bool for load (true), false for unload, a pack id, and a list of types.
    """


def release_preload_buffers():
    """
    Tell the resource system to free the memory used by the preload buffer optimization.
    """


def unregister_change_notification(callback):
    """
    unregister_change_notification(callback)
    Unregiser for a resource system callback when the filtered files change.
    """


LOT_LOAD_HITTING_THEIR_MARKS_BEGIN = 10012
LOT_LOAD_HITTING_THEIR_MARKS_END = 10013
LOT_LOAD_ON_DOOR_SETUP_BEGIN = 10018
LOT_LOAD_ON_DOOR_SETUP_END = 10019
LOT_LOAD_ON_FINALIZE_OBJECTS_BEGIN = 10032
LOT_LOAD_ON_FINALIZE_OBJECTS_END = 10033
LOT_LOAD_ON_FINAL_PLAYABLE_STATE_BEGIN = 10036
LOT_LOAD_ON_FINAL_PLAYABLE_STATE_END = 10037
LOT_LOAD_ON_HOUSEHOLD_BEGIN = 10020
LOT_LOAD_ON_HOUSEHOLD_END = 10021
LOT_LOAD_ON_INVENTORY_FIXUP_BEGIN = 10028
LOT_LOAD_ON_INVENTORY_FIXUP_END = 10029
LOT_LOAD_ON_PREMADE_SIM_FIXUP_BEGIN = 10022
LOT_LOAD_ON_PREMADE_SIM_FIXUP_END = 10023
LOT_LOAD_ON_PREROLL_BEGIN = 10030
LOT_LOAD_ON_PREROLL_END = 10031
LOT_LOAD_ON_SETUP_PORTAL_BEGIN = 10016
LOT_LOAD_ON_SETUP_PORTAL_END = 10017
LOT_LOAD_ON_SIMINFO_FIXUP_BEGIN = 10024
LOT_LOAD_ON_SIMINFO_FIXUP_END = 10025
LOT_LOAD_ON_SPAWN_SIMS_STATE_BEGIN = 10026
LOT_LOAD_ON_SPAWN_SIMS_STATE_END = 10027
LOT_LOAD_ON_SURFACE_PORTALS_BEGIN = 10034
LOT_LOAD_ON_SURFACE_PORTALS_END = 10035
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
