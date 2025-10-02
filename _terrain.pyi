"""
The _terrain module encapsulates access to the server TerrainManager.
"""

from typing import *


def adjust_locations_for_coastline(arg0, arg1):
    """
    Given a set of starting position/orientation pairs, returns the corresponding positions/orientations at the water edge. If such a location cannot be found, the identity position/orientation is returned instead.
    """


def adjust_locations_for_target_water_depth(arg0, arg1, arg2, arg3):
    """
    Given a set of starting position/orientation pairs, returns the corresponding positions/orientations at the specified water depth. If such a location cannot be found, the identity position/orientation is returned instead.
    """


def get_bounds(arg0):
    """
    Return the the min and max bounds of the world (returns a tuple of 2 Vector3 objects, representing the min and max bounds).
    """


def get_center(arg0):
    """
    Return the center of the terrain for this zone as a Vector3.
    """


def get_lot_level_height():
    """
    Return the accurate y ground height from the terrain manager at this x, z on a specific lot and level for this zone.
    """


def get_lot_level_height_and_surface_object():
    """
    Return the accurate y height and surface object id at this x, z location
    """


def get_size(arg0):
    """
    Return the size of the terrain for this zone as a Vector3.
    """


def get_snowmask_value(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
    """
    Return the snowmask value (in [0,1] range) given the position in world coordinates and the snow accumulation value.
    """


def get_water_depth():
    """
    Return the accurate water depth from the terrain manager at this x, z location for this zone.
    """


def is_position_in_bounds(arg0, arg1, arg2):
    """
    Return True if the specified point is inside the terrain bounds, False otherwise.
    """


def is_position_in_markup_region(arg0):
    """
    Return True if this position is in the world markup region.
    """


def is_terrain_tag_at_position(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None, kwarg5: Any = None, kwarg6: Any = None):
    """
    Return True if one of the specified tags is the dominant terrain tag for the location.  Note that the current implementation does not have robust handling for rugs or other lot objects.  For any location with such an object, this test will automatically return 'false' without actually checking what tags are assigned to the object.
    """
