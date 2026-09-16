# Annotations Created by TURBODRIVER

"""
Lot Module.
"""

from typing import *

import _math

class Lot():
    """
    Represents a Lot.
    """

    def __init__(self, zone_id: 'int'):
        """
        Represents a Lot.
        """

    def convert_to_lot_coordinates(self, world_transform: '_math.Transform') -> '_math.Transform':
        """
        Return a transform as a lot position when passed in a world position transform
        """

    def convert_to_world_coordinates(self, lot_transform: '_math.Transform') -> '_math.Transform':
        """
        Return a transform as a world position when passed in a lot position transform
        """

    @property
    def corners(self) -> 'Tuple[_math.Vector3, _math.Vector3, _math.Vector3, _math.Vector3]':
        """
        Returns a tuple of vectors representing the corners of the lot in world coordinates.
        """

    @corners.setter
    def corners(self, value: 'Tuple[_math.Vector3, _math.Vector3, _math.Vector3, _math.Vector3]'):
        """
        Returns a tuple of vectors representing the corners of the lot in world coordinates.
        """

    @property
    def display_level(self) -> 'int':
        """
        The display level of the lot.
        """

    @display_level.setter
    def display_level(self, value: 'int'):
        """
        The display level of the lot.
        """

    @property
    def furnished_lot_value(self) -> 'int':
        """
        Return the furnished + land value of this lot.
        """

    @furnished_lot_value.setter
    def furnished_lot_value(self, value: 'int'):
        """
        Return the furnished + land value of this lot.
        """

    def get_front_side_transforms(self, offset: 'float' = 0.5) -> 'List[_math.Transform]':
        """
        Returns a list of transforms when passed in an offset float (defaults to 0.5).  The position of the transform is calculated by taking the midpoint of a tile edge along the lot front side, then offsetting this position away from the lot interior.  The Z-axis gets transformed to point toward the lot interior.
        """

    def get_level_height(self, level: 'int') -> 'Optional[float]':
        """
        Return the height of the specified level.  If the level is invalid, returns None
        """

    def get_object_count_by_tags(self, tags: 'Sequence[int]') -> 'int':
        """
        Returns the number of objects on the lot that possess one or more of the supplied tags. For floor, roof, and wall surfaces, the number of tiles covered is used in the place of the number of objects.
        """

    def is_position_on_lot(self, position_or_x: 'Union[_math.Vector2, _math.Vector3, float]', z: 'Optional[float]' = None) -> 'bool':
        """
        Return True if the position (which can be input as a Vector2, Vector3 (y is ignored), or as 2 floats (x and z coordinates)) is on the lot, False otherwise.
        """

    @property
    def lot_id(self) -> 'int':
        """
        Return the id of this lot.
        """

    @lot_id.setter
    def lot_id(self, value: 'int'):
        """
        Return the id of this lot.
        """

    @property
    def max_allowed_level(self) -> 'int':
        """
        The maximum level that the lot is allowed to occupy.
        """

    @max_allowed_level.setter
    def max_allowed_level(self, value: 'int'):
        """
        The maximum level that the lot is allowed to occupy.
        """

    @property
    def max_level(self) -> 'int':
        """
        The maximum level of the lot.
        """

    @max_level.setter
    def max_level(self, value: 'int'):
        """
        The maximum level of the lot.
        """

    @property
    def min_allowed_level(self) -> 'int':
        """
        The minimum level that the lot is allowed to occupy.
        """

    @min_allowed_level.setter
    def min_allowed_level(self, value: 'int'):
        """
        The minimum level that the lot is allowed to occupy.
        """

    @property
    def min_level(self) -> 'int':
        """
        The minimum level of the lot.
        """

    @min_level.setter
    def min_level(self, value: 'int'):
        """
        The minimum level of the lot.
        """

    @property
    def orientation(self) -> '_math.Quaternion':
        """
        Orientation of the lot.
        """

    @orientation.setter
    def orientation(self, value: '_math.Quaternion'):
        """
        Orientation of the lot.
        """

    @property
    def owner_household_id(self) -> 'int':
        """
        (DEPRECATED, use zone_owner_household_id instead) Return the id of the household that owns this lot's zone.
        """

    @owner_household_id.setter
    def owner_household_id(self, value: 'int'):
        """
        (DEPRECATED, use zone_owner_household_id instead) Return the id of the household that owns this lot's zone.
        """

    @property
    def position(self) -> '_math.Vector3':
        """
        Position of the center of the lot.
        """

    @position.setter
    def position(self, value: '_math.Vector3'):
        """
        Position of the center of the lot.
        """

    @property
    def rotation(self) -> 'float':
        """
        Rotation of the lot.
        """

    @rotation.setter
    def rotation(self, value: 'float'):
        """
        Rotation of the lot.
        """

    @property
    def size(self) -> '_math.Vector3':
        """
        Size of the lot.
        """

    @size.setter
    def size(self, value: '_math.Vector3'):
        """
        Size of the lot.
        """

    @property
    def size_x(self) -> 'int':
        """
        Size of the lot along the X axis with no lot rotation.
        """

    @size_x.setter
    def size_x(self, value: 'int'):
        """
        Size of the lot along the X axis with no lot rotation.
        """

    @property
    def size_y(self) -> 'int':
        """
        Sum of the height of all levels of the lot.
        """

    @size_y.setter
    def size_y(self, value: 'int'):
        """
        Sum of the height of all levels of the lot.
        """

    @property
    def size_z(self) -> 'int':
        """
        Size of the lot along the Z axis with no lot rotation.
        """

    @size_z.setter
    def size_z(self, value: 'int'):
        """
        Size of the lot along the Z axis with no lot rotation.
        """

    @property
    def tile_count(self) -> 'int':
        """
        Return tile count of current lot.
        """

    @tile_count.setter
    def tile_count(self, value: 'int'):
        """
        Return tile count of current lot.
        """

    @property
    def unfurnished_lot_value(self) -> 'int':
        """
        Return the unfurnished + land value of this lot.
        """

    @unfurnished_lot_value.setter
    def unfurnished_lot_value(self, value: 'int'):
        """
        Return the unfurnished + land value of this lot.
        """

    @property
    def zone_id(self) -> 'int':
        """
        Return the zone id of this lot.
        """

    @zone_id.setter
    def zone_id(self, value: 'int'):
        """
        Return the zone id of this lot.
        """

    @property
    def zone_owner_household_id(self) -> 'int':
        """
        Return the id of the household that owns this lot's zone.
        """

    @zone_owner_household_id.setter
    def zone_owner_household_id(self, value: 'int'):
        """
        Return the id of the household that owns this lot's zone.
        """


def get_lot_id_from_instance_id(guid: 'int') -> 'int':
    """
    Convert a GUID to an Active Lot ID. Parameters:(uint64 guid)
    """
