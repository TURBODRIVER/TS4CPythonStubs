# Annotations Created by TURBODRIVER

"""
Sims4 Components Module.
"""

from typing import *

import _geometry
import _math

class _LineOfSight():
    """
    Native code for line of sight constraints for gameplay.
    """

    _connection_index: 'int'  # Index of raycast segment connections
    _interval: 'float'
    _map_divisions: 'int'  # Number of segments in _distance_map and _connections_map
    _simplification_ratio: 'float'
    build_convex: 'bool'  # Boolean that indicates whether this constaint is to contain convex polygons only

    def __init__(self, max_line_of_sight_radius: 'float', map_divisions: 'int', simplification_ratio: 'float', boundary_epsilon: 'float', build_convex: 'bool' = False):
        """
        Native code for line of sight constraints for gameplay.
        """

    def _build_convex_segments(self, points: 'Sequence[_math.Vector3]', max_segments: 'int') -> 'List[_math.Vector3]':
        """
        Extract and return a convex region in points with approximately maximum size..
        """

    def _collect_segments(self):
        """
        For all segments, if the closest point on the segment is within the _max_line_of_sight_radius,
        then we interpolate along the segment to find all collision points.
        """

    def _concave_to_convex(self, polygon: '_geometry.Polygon') -> '_geometry.CompoundPolygon':
        """
        Convert a concave polygon to multiple convex polygons and return the result.
        """

    @property
    def _connection_map(self):
        pass

    @_connection_map.setter
    def _connection_map(self, value):
        pass

    @property
    def _contours(self):
        pass

    @_contours.setter
    def _contours(self, value):
        pass

    @property
    def _distance_map(self):
        pass

    @_distance_map.setter
    def _distance_map(self, value):
        pass

    def _get_intersection(self, segment_a: 'Tuple[_math.Vector3, _math.Vector3]', segment_b: 'Tuple[_math.Vector3, _math.Vector3]') -> 'Optional[_math.Vector3]':
        """
        Convert a concave polygon to multiple convex polygons and return the result.
        """

    def _make_compound_polygon(self, polygons: 'Sequence[_geometry.Polygon]') -> '_geometry.CompoundPolygon':
        """
        Extract and return a convex region in points with approximately maximum size..
        """

    @property
    def _max_line_of_sight_radius(self) -> 'float':
        """
        Max line of sight for this Constraint.  Setting this will also set _max_line_of_sight_radius_sq
        """

    @_max_line_of_sight_radius.setter
    def _max_line_of_sight_radius(self, value: 'float'):
        """
        Max line of sight for this Constraint.  Setting this will also set _max_line_of_sight_radius_sq
        """

    @property
    def _max_line_of_sight_radius_sq(self) -> 'float':
        pass

    @_max_line_of_sight_radius_sq.setter
    def _max_line_of_sight_radius_sq(self, value: 'float'):
        pass

    @property
    def _position(self) -> '_math.Vector3':
        pass

    @_position.setter
    def _position(self, value: '_math.Vector3'):
        pass

    def _render_vertices(self) -> 'List[_math.Vector3]':
        """
        Return the vertices associated with the last ray-cast performed by this LOS component.
        
        Note that this polygon should be simplified before use, because it may contain redundant vertices.
        """

    def _simplify_geometry(self, vertices: 'Sequence[_math.Vector3]', origin: 'Optional[_math.Vector3]' = None) -> 'List[_math.Vector3]':
        """
        Reduce the number of points in the generated polygon, and return the result.
        
        The simplified polygon must contain the origin, if one is given.
        
        vertices: An iterable containing unsimplified vertices.  Expected to be in correct winding order.
        origin: If not None, edges will not be simplified if they would exclude this origin.
        """

    def maximal_convex(self, points: 'Sequence[_math.Vector3]') -> '_geometry.Polygon':
        """
        Extract and return the convex region in points with the maximum size.
        """
