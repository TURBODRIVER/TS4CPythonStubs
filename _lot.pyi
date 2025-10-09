"""
Lot Module.
"""

from typing import *


class Lot():
    """
    Represents a Lot.
    """

    def __init__(self, arg0):
        pass

    def convert_to_lot_coordinates(self, arg0):
        """
        Return a transform as a lot position when passed in a world position transform
        """

    def convert_to_world_coordinates(self, arg0):
        """
        Return a transform as a world position when passed in a lot position transform
        """

    @property
    def corners(self):
        """
        Returns a tuple of vectors representing the corners of the lot in world coordinates.
        """

    @corners.setter
    def corners(self, value):
        """
        Returns a tuple of vectors representing the corners of the lot in world coordinates.
        """

    @property
    def display_level(self):
        """
        The display level of the lot.
        """

    @display_level.setter
    def display_level(self, value):
        """
        The display level of the lot.
        """

    @property
    def furnished_lot_value(self):
        """
        Return the furnished + land value of this lot.
        """

    @furnished_lot_value.setter
    def furnished_lot_value(self, value):
        """
        Return the furnished + land value of this lot.
        """

    def get_front_side_transforms(self):
        """
        Returns a list of transforms when passed in an offset float (defaults to 0.5).  The position of the transform is calculated by taking the midpoint of a tile edge along the lot front side, then offsetting this position away from the lot interior.  The Z-axis gets transformed to point toward the lot interior.
        """

    def get_level_height(self, arg0):
        """
        Return the height of the specified level.  If the level is invalid, returns None
        """

    def get_object_count_by_tags(self, arg0):
        """
        Returns the number of objects on the lot that possess one or more of the supplied tags. For floor, roof, and wall surfaces, the number of tiles covered is used in the place of the number of objects.
        """

    def is_position_on_lot(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
        """
        Return True if the position (which can be input as a Vector2, Vector3 (y is ignored), or as 2 floats (x and z coordinates)) is on the lot, False otherwise.
        """

    @property
    def lot_id(self):
        """
        Return the id of this lot.
        """

    @lot_id.setter
    def lot_id(self, value):
        """
        Return the id of this lot.
        """

    @property
    def max_allowed_level(self):
        """
        The maximum level that the lot is allowed to occupy.
        """

    @max_allowed_level.setter
    def max_allowed_level(self, value):
        """
        The maximum level that the lot is allowed to occupy.
        """

    @property
    def max_level(self):
        """
        The maximum level of the lot.
        """

    @max_level.setter
    def max_level(self, value):
        """
        The maximum level of the lot.
        """

    @property
    def min_allowed_level(self):
        """
        The minimum level that the lot is allowed to occupy.
        """

    @min_allowed_level.setter
    def min_allowed_level(self, value):
        """
        The minimum level that the lot is allowed to occupy.
        """

    @property
    def min_level(self):
        """
        The minimum level of the lot.
        """

    @min_level.setter
    def min_level(self, value):
        """
        The minimum level of the lot.
        """

    @property
    def orientation(self):
        """
        Orientation of the lot.
        """

    @orientation.setter
    def orientation(self, value):
        """
        Orientation of the lot.
        """

    @property
    def owner_household_id(self):
        """
        (DEPRECATED, use zone_owner_household_id instead) Return the id of the household that owns this lot's zone.
        """

    @owner_household_id.setter
    def owner_household_id(self, value):
        """
        (DEPRECATED, use zone_owner_household_id instead) Return the id of the household that owns this lot's zone.
        """

    @property
    def position(self):
        """
        Position of the center of the lot.
        """

    @position.setter
    def position(self, value):
        """
        Position of the center of the lot.
        """

    @property
    def rotation(self):
        """
        Rotation of the lot.
        """

    @rotation.setter
    def rotation(self, value):
        """
        Rotation of the lot.
        """

    @property
    def size(self):
        """
        Size of the lot.
        """

    @size.setter
    def size(self, value):
        """
        Size of the lot.
        """

    @property
    def size_x(self):
        """
        Size of the lot along the X axis with no lot rotation.
        """

    @size_x.setter
    def size_x(self, value):
        """
        Size of the lot along the X axis with no lot rotation.
        """

    @property
    def size_y(self):
        """
        Sum of the height of all levels of the lot.
        """

    @size_y.setter
    def size_y(self, value):
        """
        Sum of the height of all levels of the lot.
        """

    @property
    def size_z(self):
        """
        Size of the lot along the Z axis with no lot rotation.
        """

    @size_z.setter
    def size_z(self, value):
        """
        Size of the lot along the Z axis with no lot rotation.
        """

    @property
    def tile_count(self):
        """
        Return tile count of current lot.
        """

    @tile_count.setter
    def tile_count(self, value):
        """
        Return tile count of current lot.
        """

    @property
    def unfurnished_lot_value(self):
        """
        Return the unfurnished + land value of this lot.
        """

    @unfurnished_lot_value.setter
    def unfurnished_lot_value(self, value):
        """
        Return the unfurnished + land value of this lot.
        """

    @property
    def zone_id(self):
        """
        Return the zone id of this lot.
        """

    @zone_id.setter
    def zone_id(self, value):
        """
        Return the zone id of this lot.
        """

    @property
    def zone_owner_household_id(self):
        """
        Return the id of the household that owns this lot's zone.
        """

    @zone_owner_household_id.setter
    def zone_owner_household_id(self, value):
        """
        Return the id of the household that owns this lot's zone.
        """


def get_lot_id_from_instance_id(uint64guid):
    """
    Convert a GUID to an Active Lot ID. Parameters:(uint64 guid)
    """
