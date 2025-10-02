"""
Sims4 Components Module.
"""


class _LineOfSight():
    """
    Native code for line of sight constraints for gameplay.
    """

    def __init__(self, arg0, arg1, arg2, arg3, arg4):
        _connection_index: Any  # Index of raycast segment connections
        _interval: Any
        _map_divisions: Any  # Number of segments in _distance_map and _connections_map
        _simplification_ratio: Any
        build_convex: Any  # Boolean that indicates whether this constaint is to contain convex polygons only

    def _build_convex_segments(self, arg0, arg1):
        """
        Extract and return a convex region in points with approximately maximum size..
        """

    def _collect_segments(self):
        """
        For all segments, if the closest point on the segment is within the _max_line_of_sight_radius,
        then we interpolate along the segment to find all collision points.
        """

    def _concave_to_convex(self, arg0):
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

    def _get_intersection(self, arg0, arg1):
        """
        Convert a concave polygon to multiple convex polygons and return the result.
        """

    def _make_compound_polygon(self, arg0):
        """
        Extract and return a convex region in points with approximately maximum size..
        """

    @property
    def _max_line_of_sight_radius(self):
        """
        Max line of sight for this Constraint.  Setting this will also set _max_line_of_sight_radius_sq
        """

    @_max_line_of_sight_radius.setter
    def _max_line_of_sight_radius(self, value):
        """
        Max line of sight for this Constraint.  Setting this will also set _max_line_of_sight_radius_sq
        """

    @property
    def _max_line_of_sight_radius_sq(self):
        pass

    @_max_line_of_sight_radius_sq.setter
    def _max_line_of_sight_radius_sq(self, value):
        pass

    @property
    def _position(self):
        pass

    @_position.setter
    def _position(self, value):
        pass

    def _render_vertices(self):
        """
        Return the vertices associated with the last ray-cast performed by this LOS component.
        
        Note that this polygon should be simplified before use, because it may contain redundant vertices.
        """

    def _simplify_geometry(self):
        """
        Reduce the number of points in the generated polygon, and return the result.
        
        The simplified polygon must contain the origin, if one is given.
        
        vertices: An iterable containing unsimplified vertices.  Expected to be in correct winding order.
        origin: If not None, edges will not be simplified if they would exclude this origin.
        """

    def maximal_convex(self, arg0):
        """
        Extract and return the convex region in points with the maximum size.
        """
