# Annotations Created by TURBODRIVER

"""
The _terrain module encapsulates access to the server TerrainManager.
"""

from typing import *

import _math

def adjust_locations_for_coastline(zone_id: 'int', initial_transforms: 'Sequence[_math.Transform]') -> 'List[_math.Transform]':
    """
    Given a set of starting position/orientation pairs, returns the corresponding positions/orientations at the water edge. If such a location cannot be found, the identity position/orientation is returned instead.
    """


def adjust_locations_for_target_water_depth(zone_id: 'int', target_depth: 'float', error: 'float', initial_transforms: 'Sequence[_math.Transform]') -> 'List[_math.Transform]':
    """
    Given a set of starting position/orientation pairs, returns the corresponding positions/orientations at the specified water depth. If such a location cannot be found, the identity position/orientation is returned instead.
    """


def get_bounds(zone_id: 'int') -> 'Tuple[float, float, float, float]':
    """
    Return the the min and max bounds of the world (returns a tuple of 2 Vector3 objects, representing the min and max bounds).
    """


def get_center(zone_id: 'int') -> 'Tuple[float, float]':
    """
    Return the center of the terrain for this zone as a Vector3.
    """


def get_lot_level_height(x: 'float', z: 'float', zone_id: 'int', level: 'int') -> 'float':
    """
    Return the accurate y ground height from the terrain manager at this x, z on a specific lot and level for this zone.
    """


def get_lot_level_height_and_surface_object(x: 'float', z: 'float', zone_id: 'int', level: 'int') -> 'Tuple[float, int]':
    """
    Return the accurate y height and surface object id at this x, z location
    """


def get_size(zone_id: 'int') -> 'Tuple[float, float]':
    """
    Return the size of the terrain for this zone as a Vector3.
    """


def get_snowmask_value(x: 'float', z: 'float', zone_id: 'int') -> 'float':
    """
    Return the snowmask value (in [0,1] range) given the position in world coordinates and the snow accumulation value.
    """


def get_water_depth(x: 'float', z: 'float', zone_id: 'int', level: 'int' = 0) -> 'float':
    """
    Return the accurate water depth from the terrain manager at this x, z location for this zone.
    """


def is_position_in_bounds(x: 'float', z: 'float', zone_id: 'int') -> 'bool':
    """
    Return True if the specified point is inside the terrain bounds, False otherwise.
    """


def is_position_in_markup_region(position: '_math.Vector3') -> 'bool':
    """
    Return True if this position is in the world markup region.
    """


def is_terrain_tag_at_position(x: 'float', z: 'float', zone_id: 'int', tag_values: 'Sequence[int]', level: 'int' = 0, required_strength: 'float' = 0.75, test_floor_tiles: 'bool' = False) -> 'bool':
    """
    Return True if one of the specified tags is the dominant terrain tag for the location.  Note that the current implementation does not have robust handling for rugs or other lot objects.  For any location with such an object, this test will automatically return 'false' without actually checking what tags are assigned to the object.
    """
