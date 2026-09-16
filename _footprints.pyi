# Annotations Created by TURBODRIVER

"""
Footprints
"""

import _geometry

class PolygonFootprint():
    """
    PolygonFootprint(polygon:Polygon, cost:float=0.0f, enabled:bool=False, footprint_type=kFootprintType_Override)
    """

    def __init__(self, polygon: '_geometry.Polygon', cost: 'float' = 0.0, enabled: 'bool' = False, footprint_type: 'int' = 0):
        """
        PolygonFootprint(polygon:Polygon, cost:float=0.0f, enabled:bool=False, footprint_type=kFootprintType_Override)
        """

    def __getitem__(self, key: 'int'):
        """
        Return self[key].
        """

    def __len__(self) -> 'int':
        """
        Return len(self).
        """

    @property
    def cost(self) -> 'float':
        """
        The cost of traversing this footprint.
        
        Values less than 1.0f represent encouragement. Values greater than 1.0f represent discouragement.
        """

    @cost.setter
    def cost(self, value: 'float'):
        """
        The cost of traversing this footprint.
        
        Values less than 1.0f represent encouragement. Values greater than 1.0f represent discouragement.
        """

    @property
    def enabled(self) -> 'bool':
        """
        The footprint is active in the nav mesh.
        """

    @enabled.setter
    def enabled(self, value: 'bool'):
        """
        The footprint is active in the nav mesh.
        """

    @property
    def footprint_id(self) -> 'int':
        """
        The id of this footprint.
        """

    @footprint_id.setter
    def footprint_id(self, value: 'int'):
        """
        The id of this footprint.
        """

    @property
    def footprint_type(self) -> 'int':
        """
        The type of this footprint.
        """

    @footprint_type.setter
    def footprint_type(self, value: 'int'):
        """
        The type of this footprint.
        """

    @property
    def polygon(self) -> '_geometry.Polygon':
        """
        The polygon this footprint represents in the nav mesh.
        """

    @polygon.setter
    def polygon(self, value: '_geometry.Polygon'):
        """
        The polygon this footprint represents in the nav mesh.
        """

    def set_global_enabled(self, enabled: 'bool'):
        """
        set_global_enabled(enabled:bool)
        """
