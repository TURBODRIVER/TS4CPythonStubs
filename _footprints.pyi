"""
Footprints
"""

from typing import *


class PolygonFootprint():
    """
    PolygonFootprint(polygon:Polygon, cost:float=0.0f, enabled:bool=False, footprint_type=kFootprintType_Override)
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
        pass

    def __getitem__(self):
        """
        Return self[key].
        """

    def __len__(self):
        """
        Return len(self).
        """

    @property
    def cost(self):
        """
        The cost of traversing this footprint.
        
        Values less than 1.0f represent encouragement. Values greater than 1.0f represent discouragement.
        """

    @cost.setter
    def cost(self, value):
        """
        The cost of traversing this footprint.
        
        Values less than 1.0f represent encouragement. Values greater than 1.0f represent discouragement.
        """

    @property
    def enabled(self):
        """
        The footprint is active in the nav mesh.
        """

    @enabled.setter
    def enabled(self, value):
        """
        The footprint is active in the nav mesh.
        """

    @property
    def footprint_id(self):
        """
        The id of this footprint.
        """

    @footprint_id.setter
    def footprint_id(self, value):
        """
        The id of this footprint.
        """

    @property
    def footprint_type(self):
        """
        The type of this footprint.
        """

    @footprint_type.setter
    def footprint_type(self, value):
        """
        The type of this footprint.
        """

    @property
    def polygon(self):
        """
        The polygon this footprint represents in the nav mesh.
        """

    @polygon.setter
    def polygon(self, value):
        """
        The polygon this footprint represents in the nav mesh.
        """

    def set_global_enabled(self, enabled: bool):
        pass
