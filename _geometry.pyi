"""
Geometry Utilities
"""

from typing import *


class AbsoluteOrientationRange():
    """
    an absolute orientation range.
    The facing and angle are given in radians.
    Orientation is restricted to be within angle/2 of facingAn orientation restriction that is an absolute range (in radians).
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
        pass

    @property
    def interval(self):
        """
        Interval
        """

    @interval.setter
    def interval(self, value):
        """
        Interval
        """

    def range(self, arg0):
        """
        Gets the interval at the specified point.  ARGS: (Vector3)point
        """

    def set_params(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
        """
        Sets Params for scoring function.  Points are scored by measuring distance from line formed by initial point and angle, then normalized to [0,1] where distance < ideal_distance is scored as 1, ideal_distance < distance < max_distance is scored as 1->0, and distance >= max_distance is scored as 0.  ARGS: (Vector3)point1, (Vector3)point2, (float)ideal_distance, (float)max_distance
        """


class AngularInterval():
    """
    AngularInterval(minAngle, maxAngle) -> a clockwise angular interval (circular arc) between min and max angles (measured in radians).
    An interval must also have an ideal angle (and weight) which is
    respected when intersecting two intervals.  The ideal angle is used to select
    which segment is selected when and intersection of two concave intervals
    results in disjoint regions.
    
    An angular interval is defined by two angles, a and b.  Because angles
    are equivalent modulo 2 * Pi, we need to normalize the interval.  The
    normalization rules are: a is in [0, 2 * Pi), and b is in [a, a + 2 * Pi].
    
    The size of the angular interval is cached.
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None):
        pass

    @property
    def ALL(self):
        """
        Angular Interval that allows all angles. [0,2PI).
        """

    @ALL.setter
    def ALL(self, value):
        """
        Angular Interval that allows all angles. [0,2PI).
        """

    @property
    def NONE(self):
        """
        Angular Interval that allows no angles.
        """

    @NONE.setter
    def NONE(self, value):
        """
        Angular Interval that allows no angles.
        """

    def __bool__(self):
        """
        self != 0
        """

    def __contains__(self):
        """
        Return key in self.
        """

    @property
    def a(self):
        """
        Minimum Angle
        """

    @a.setter
    def a(self, value):
        """
        Minimum Angle
        """

    @property
    def angle(self):
        """
        Angle
        """

    @angle.setter
    def angle(self, value):
        """
        Angle
        """

    @property
    def b(self):
        """
        Maximum Angle
        """

    @b.setter
    def b(self, value):
        """
        Maximum Angle
        """

    def clamp(self, arg0):
        """
        Clamp the given angle within this interval.  If the angle is contained within the interval, return the angle.  Otherwise, return the closest end point.
        """

    def contains_angle(self, arg0):
        """
        returns True if the AngularInterval contains the specified angle.
        """

    def get_distance(self, arg0):
        """
        Return the angular distance from this interval to the given angle.
        If angle is contained in this interval, distance is zero.  Otherwise,
        the distance is the angle from the nearest boundary to the given angle.
        """

    @property
    def ideal(self):
        """
        Ideal Angle
        """

    @ideal.setter
    def ideal(self, value):
        """
        Ideal Angle
        """

    def intersect(self, arg0):
        """
        Intersect two angular intervals.
        """

    @property
    def is_none(self):
        """
        Is the Interval None
        """

    @is_none.setter
    def is_none(self, value):
        """
        Is the Interval None
        """

    def set(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None):
        """
        Sets min and max angle.
        """

    def set_ideal_angle(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        Set the ideal angle (and optional weight) for this interval.
        """

    def set_to_none(self, *args):
        """
        Sets to None.
        """

    @property
    def weight(self):
        """
        Weight
        """

    @weight.setter
    def weight(self, value):
        """
        Weight
        """


class Circle():
    """
    Circle(center, radius) -> A new circle.  'center' must be a Vector2
    """

    def __init__(self, arg0, arg1):
        pass

    @property
    def center(self):
        """
        The center of the circle, as Vector2(x, z)
        """

    @center.setter
    def center(self, value):
        """
        The center of the circle, as Vector2(x, z)
        """

    @property
    def radius(self):
        """
        The radius of the circle
        """

    @radius.setter
    def radius(self, value):
        """
        The radius of the circle
        """


class CompoundPolygon():
    """
    Array of Polygons.
    """

    def __init__(self, *args):
        pass

    def __bool__(self):
        """
        self != 0
        """

    def __getitem__(self):
        """
        Return self[key].
        """

    def __len__(self):
        """
        Return len(self).
        """

    def area(self):
        """
        CompoundPoly.area()
        Return the area of all of the polygons in the compound polygon.
        """

    def bounds(self):
        """
        CompoundPoly.bounds()
        Return the AABB (Vec3 min, Vec3 max)of all of the polygons in the compound polygon.
        """

    def centroid(self):
        """
        CompoundPoly.centroid()
        Return the centroid of all of the polygons in the compound polygon.
        """

    def contains(self, arg0):
        """
        CompoundPoly.contains()
        Return if the Compound Polygon contains the provided vertex.
        """

    @property
    def convex(self):
        """
        CompoundPoly.convex()
        Return True, we currently only store convex polygons in a compound polygon.
        """

    @convex.setter
    def convex(self, value):
        """
        CompoundPoly.convex()
        Return True, we currently only store convex polygons in a compound polygon.
        """

    @property
    def has_enough_vertices(self):
        """
        CompoundPoly.has_enough_vertices()
        Return true if we have at least one polygon and all polygons have at least one vertex.
        """

    @has_enough_vertices.setter
    def has_enough_vertices(self, value):
        """
        CompoundPoly.has_enough_vertices()
        Return true if we have at least one polygon and all polygons have at least one vertex.
        """

    def intersect(self, arg0):
        """
        CompoundPolyA.intersect(CompoundPolyB) -> CompoundPolygon
        Return a CompoundPolygon that's the intersection of CompoundPolyA and CompoundPolyB.
        """

    def intersects(self, arg0):
        """
        CompoundPolyA.intersects(CompoundPolyB) -> CompoundPolygon
        Return whether or not CompoundPolyA intersects CompoundPolyB.
        """

    def radius(self):
        """
        CompoundPoly.radius()
        Return the max radius of all of the polygons in the compound polygon.
        """

    def union(self, arg0):
        """
        CompoundPolyA.union(CompoundPolyB) -> CompoundPolygon
        Return a CompoundPolygon that's the union of CompoundPolyA and CompoundPolyB.
        Note: Simply combines the lists of associated polygons.  Does not remove overlap.
        """


OBJECT_QUAD_TREE_QUERY_FLAG_IGNORE_BOUNDS = 1
OBJECT_QUAD_TREE_QUERY_FLAG_IGNORE_SURFACE = 2
OBJECT_QUAD_TREE_QUERY_FLAG_IGNORE_SURFACE_TYPE = 4
OBJECT_QUAD_TREE_QUERY_FLAG_MUST_NOT_CONTAIN_QUERY_BOUNDS = 16
OBJECT_QUAD_TREE_QUERY_FLAG_ONLY_FULLY_CONTAINED = 8
OBJECT_QUAD_TREE_QUERY_FLAG_STOP_AT_FIRST_RESULT = 32


class Polygon():
    """
    Polygon(vertices) -> A new polygon.  Vertices must be a sequence of Vector3.
    """

    def __init__(self):
        pass

    def __bool__(self):
        """
        self != 0
        """

    def __getitem__(self):
        """
        Return self[key].
        """

    def __len__(self):
        """
        Return len(self).
        """

    def add(self, arg0):
        """
        p.add(Vector2 or Vector3 p) -> None
        Adds the point p at end of the polygon.  Note that this is more efficient than calling insert as the polygon is internally stored as an array.
        """

    def area(self):
        """
        p.area() -> float
        The area of this polygon projected onto the (x,z) plane.
        """

    def average_radius(self):
        """
        p.average_radius() -> float
        Returns the average of radius and min_radius.
        """

    def bounds(self):
        """
        p.bounds() -> (Vector3 min, Vector3 max)
        Returns the min and max points defining the AABB for this polygon.
        """

    @property
    def ccw(self):
        """
        True if polygon is counterclockwise.
        """

    @ccw.setter
    def ccw(self, value):
        """
        True if polygon is counterclockwise.
        """

    def centroid(self):
        """
        p.centroid() -> Vector3
        Returns the centroid of the polygon.
        """

    def compare_vectors_ccw(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        Polygon.compare_vectors_ccw(a:Vector3, b:Vector3) -> int
        Return 1 if a > b, -1 if a < b and 0 if a == b
        """

    def contains(self, arg0):
        """
        p.contains(Polygon, Vector2, or Vector3) -> bool
        Whether the polygon contains the specified polygon or point.
        """

    @property
    def convex(self):
        """
        True if polygon is convex.  Note that 1 and 2 point polygons are considered convex.
        """

    @convex.setter
    def convex(self, value):
        """
        True if polygon is convex.  Note that 1 and 2 point polygons are considered convex.
        """

    @property
    def degenerate(self):
        """
        True if polygon is degenerate (i.e. has overlapping and/or collinear vertices).
        """

    @degenerate.setter
    def degenerate(self, value):
        """
        True if polygon is degenerate (i.e. has overlapping and/or collinear vertices).
        """

    def force_ccw(self):
        """
        p.force_ccw() -> None
        Checks if the Polygon is CCW and if not (and it is valid), reverses the vertices so that it is CCW.
        """

    def get_closest_edge_to_point(self, arg0):
        """
        p.get_closest_edge_to_point(Vector2/Vector3 p) -> (int, float, Vector3)
        Returns a tuple containing the index i of the edge (i,i+1) that is the closest edge to p,
        the distance between p to the closest point on that edge, and the point on the edge closest to p.
        If the Polygon is empty, returns None.
        """

    def get_closest_point_in_polygon_to_point(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        p.get_closest_point_in_polygon_to_point(Vector2/Vector3 p, float minDist = 0) -> (int, Vector3)
        Returns a tuple containing the index i of the edge (i,i+1) that is the closest edge to p
        and the point inside the polygon.  If minDist > 0, the point will be at least minDist away from the edge.
        If the polygon is invalid or no valid point can be found that is at least minDist away from all edges and
        still inside the polygon, returns None.
        """

    def get_convex_hull(self):
        """
        p.get_convex_hull() -> Polygon
        Returns a Polygon that is the Convex Hull of the current Polygon.
        If the current Polygon is already convex, the returned Polygon will be a duplicate.
        Returns None if the Polygon is invalid.
        """

    def get_distance_to_circle(self, arg0):
        """
        p.get_distance_to_circle(Circle c) -> (float dist, bool intersects, int edgeIdx, Vector3 closestPoint)
        Returns a tuple containing:
            1. the minimum distance between the polygon and the specified circle
            2. True/False if the polygon intersects the circle
            3. Index of the edge that is closest to the circle
            4. The closest point on the polygon to the circle
        Returns None if the polygon or Circle are empty or otherwise invalid.
        """

    def get_distance_to_point(self, arg0):
        """
        p.get_distance_to_point(Vector2/Vector3 p) -> (float dist, bool intersects, int edgeIdx, Vector3 closestPoint)
        Returns a tuple containing:
            1. the minimum distance between the polygon and the specified point
            2. True/False if the polygon intersects the point
            3. Index of the edge that is closest to p
            4. The closest point on the polygon to p
        Returns None if the polygon is empty or otherwise invalid.
        """

    def get_distance_to_polygon(self, arg0):
        """
        p.get_distance_to_polygon(Polygon c) -> (float dist, bool intersects, int edgeIdx, Vector3 closestPoint)
        Returns a tuple containing:
            1. the minimum distance between the polygon and the specified polygon
            2. True/False if the polygon intersects the polygon
            3. Index of the edge that is closest to the polygon
            4. The closest point on the polygon to the polygon
        Returns None if either polygon is empty or otherwise invalid.
        """

    def get_distance_to_rect(self, arg0):
        """
        p.get_distance_to_rect(Rect r) -> (float dist, bool intersects, int edgeIdx, Vector3 closestPoint)
        Returns a tuple containing:
            1. the minimum distance between the polygon and the specified rect
            2. True/False if the polygon intersects the rect
            3. Index of the edge that is closest to the rect
            4. The closest point on the polygon to the rect
        Returns None if the polygon or Rect are empty or otherwise invalid.
        """

    def get_distance_to_segment(self, arg0, arg1):
        """
        p.get_distance_to_segment(Vector2/Vector3 segStart, Vector2/Vector3 segEnd) -> (float dist, bool intersects, int edgeIdx, Vector3 closestPoint)
        Returns a tuple containing:
            1. the minimum distance between the polygon and the specified segment
            2. True/False if the polygon intersects the segment
            3. Index of the edge that is closest to the segment
            4. The closest point on the polygon to the segment
        Returns None if the polygon is empty or otherwise invalid.
        """

    def get_error_string(self):
        """
        p.get_error_string() -> string
        If the polygon is not valid, this will return a string describing the errors.   If the polygon is valid, this returns an empty string.
        """

    def get_normals(self):
        """
        p.get_normals() -> (Vector3, Vector3, ..)
        Returns a tuple of Vector3 objects, each of which is a normal of the corresponding vertex in the Polygon.
        Returns None if the Polygon is invalid.
        """

    def get_octant_and_slope(self, kwarg0: Any = None):
        """
        Polygon.get_octant_and_slope(v:Vector3) -> (octant:int, slope:float)
        """

    def get_vertex_farthest_in_direction(self, arg0):
        """
        p.get_vertex_farthest_in_direction(Vector2/Vector3 dirNormalized) -> int
        Returns index of the vertex in the polygon that is the farthest along in the specified direction.
        Only works on Convex polygons.   dirNormalized MUST be normalized already.  Returns None if Polygon is invalid or concave.
        """

    @property
    def has_collinear_vertices(self):
        """
        True if polygon has any collinear vertices (i.e. any 3 coincident vertices that form a straight line).
        """

    @has_collinear_vertices.setter
    def has_collinear_vertices(self, value):
        """
        True if polygon has any collinear vertices (i.e. any 3 coincident vertices that form a straight line).
        """

    @property
    def has_duplicated_consecutive_vertices(self):
        """
        True if polygon has any coincident vertices that overlap or are "too close" together (currently 0.0001).
        """

    @has_duplicated_consecutive_vertices.setter
    def has_duplicated_consecutive_vertices(self, value):
        """
        True if polygon has any coincident vertices that overlap or are "too close" together (currently 0.0001).
        """

    @property
    def has_enough_vertices(self):
        """
        True if polygon has 1 or more vertex.
        """

    @has_enough_vertices.setter
    def has_enough_vertices(self, value):
        """
        True if polygon has 1 or more vertex.
        """

    def index_of(self, arg0):
        """
        p.index_of(Vector2 or Vector3 p) -> int
        Returns the first index of the polygon that is equal to the specified point p.   If no match is found, returns None.
        """

    def inflate(self, arg0):
        """
        p.inflate(float amt) -> None
        Inflates (or deflates if amt is negative) the Polygon by the specified amount.  Currently only works on Convex Polygons.
        Cannot deflate polygon past a minimum size less than PI * delta.  Does nothing if the delta is too small, the polygon is invalid,
        the polygon has fewer than 3 points, or some other internal error occurs.
        """

    def insert(self, arg0, arg1):
        """
        p.insert(i, Vector2 or Vector3 p) -> None
        Inserts the point p at index i.
        """

    def intersect(self, kwarg0: Any = None):
        """
        p.intersect(other) -> Polygon
        A new polygon that is the intersect of p and other.   TODO: return a tuple of polygons instead of just 1 since intersection of concave polygon can give more than 1 result.
        """

    def intersects(self, arg0):
        """
        p.intersects(Polygon, Rect, or Circle) -> bool
        Returns true if the polygon intersects the specified geometry object.
        """

    def min_radius(self):
        """
        p.min_radius() -> float
        Returns the distance from the centroid to the nearest point on any edge.
        """

    def move_to(self, arg0):
        """
        p.move_to(Vector3) -> None
        Translate the polygon such that the centroid is in the specified position.
        """

    def normalize(self):
        """
        p.normalize() -> Polygon
        A new polygon with coordinate and colinear vertices removed.
        """

    def perimeter(self):
        """
        p.perimeter() -> float
        Returns sum of the length of all sides of this polygon.
        """

    def pick_edge(self, arg0, arg1):
        """
        p.pick_edge(Vector2/Vector3 p, float epsilonSquared) -> (int, float)
        Returns a tuple of the index i of the edge (i,i+1) that is the closest edge to p and less than
        epsilonSquared m^2 to p and the distance to the edge.  Returns None if no valid edge is found.
        Note that the p MUST be "on" the segment for a value to be returned.  For example, if the segment is
        (0,0) -> (1,0), the x value of p MUST be in the range [0,1].  p(-0.001, 0.0) would fail because it is
        outside the length of the segment no matter how large the epsilon.  However, p(0.00001, .5) with an epsilon
        of 0.250001 would work.   Remember that the epsilon is used against the SQUARED distance estimates.
        """

    def pick_vertex(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
        """
        p.pick_vertex(Vector2/Vector3 p, float epsilonSquared, bool bReturnFirstFound = False) -> int
        Returns the index of the vertex which is closest to p and within epsilonSquared distance-squared
        of p or None if there is no such a vertex.
        If bReturnFirstFound is true, returns the index of the first vertex checked that is within
        epsilonSquared distance-squared of p
        .
        """

    def pop_back(self):
        """
        p.pop_back() -> Vector3
        Removes the last vertex of the Polygon (and returns it).  Note that this is more efficient than calling remove as the polygon is internally stored as an array.
        """

    def radius(self):
        """
        p.radius() -> float
        Returns the distance from the centroid to the farthest vertex from the centroid.
        """

    def remove(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        p.remove(i, n = 1) -> None
        Removes n vertices (default = 1) starting at index i.
        """

    def rotate(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        p.rotate(float r, Vector3 ctr = centroid) -> None
        Rotates the polygon around the specified ctr point (or the centroid if no point is provided) by r radians.
        """

    def sample(self):
        """
        p.sample() -> Vector3
        Returns a random point guaranteed to be within the Polygon.
        If the Polygon is invalid, returns None.
        """

    def scale(self, arg0):
        """
        p.scale(float s) -> None
        Scales Polygon by specified amount.  Note that this can cause problems for concave polygons and could make them complex.  Convex polygons should work if the scale doesn't go too low.
        """

    @property
    def simple(self):
        """
        True if polygon is simple (i.e. is not self-intersecting).  Note that having duplicate vertices will fail this condition as well.
        """

    @simple.setter
    def simple(self, value):
        """
        True if polygon is simple (i.e. is not self-intersecting).  Note that having duplicate vertices will fail this condition as well.
        """

    def split_complex(self):
        """
        p.split_complex() -> (Polygon1, Polygon2, ...)
        Returns a tuple of simple polygons formed by splitting a complex polygon.
        """

    def subtract(self, arg0):
        """
        p.subtract(other) -> (Polygon1, Polygon2, ...)
        Returns a tuple of polygons formed by subtracting other from this polygon.
        """

    @property
    def too_small(self):
        """
        True if polygon's |area| is less than GEO_FACE_MIN_AREA (currently 0.000000433012701892219).
        """

    @too_small.setter
    def too_small(self, value):
        """
        True if polygon's |area| is less than GEO_FACE_MIN_AREA (currently 0.000000433012701892219).
        """

    @property
    def too_thin(self):
        """
        True if polygon contains any regions that are too thin (i.e. if the cross product of the normals of any 2 coincident vertices is less than 2 degrees (~0.0349 radians)
        """

    @too_thin.setter
    def too_thin(self, value):
        """
        True if polygon contains any regions that are too thin (i.e. if the cross product of the normals of any 2 coincident vertices is less than 2 degrees (~0.0349 radians)
        """

    def translate(self, arg0):
        """
        p.translate(Vector3) -> None
        Translate the polygon by the specified amount.
        """

    def union(self, arg0):
        """
        p.union(other) -> (Polygon1, Polygon2, ...)
        Returns a tuple of polygons formed by taking the union of the two polygons.
        """

    def valid(self, kwarg0: Any = None):
        """
        p.too_small(ForceCheck = False)() -> bool
        Returns true if the polygon has 3 or more vertices, is not degenerate, is simple, and the area is not too small to form a valid polygon.
        """


class QuadTree():
    """
    QuadTree() -> A QuadTree used for efficient spatial queries in 2D
    """

    def __init__(self, *args):
        pass

    def insert(self, arg0, arg1):
        """
        qt.insert(object, bounds)
        Inserts 'object' into the QuadTree with the specified bounds, or modifies the bounds for an existing object
        """

    def query(self, arg0):
        """
        qt.query(bounds) -> [object, ...]
        A list of objects which were found within 'bounds'
        """

    def remove(self, arg0):
        """
        qt.remove(object)
        Removes 'object' from the QuadTree
        """


class Rect():
    """
    Rect(a, b) -> A new Rect.  a and b must be Vector2s.
    a - the 'minimum' corner of the rectangle
    b - the 'maximum' corner of the rectangle
    """

    def __init__(self, arg0, arg1):
        pass

    @property
    def a(self):
        """
        The 'minimum' corner of the rectangle, as Vector2(min_x, min_z)
        """

    @a.setter
    def a(self, value):
        """
        The 'minimum' corner of the rectangle, as Vector2(min_x, min_z)
        """

    @property
    def b(self):
        """
        The 'maximum' corner of the rectangle, as Vector2(max_x, max_z)
        """

    @b.setter
    def b(self, value):
        """
        The 'maximum' corner of the rectangle, as Vector2(max_x, max_z)
        """


class RelativeFacingRange():
    """
    An orientation restriction facing relative to a fixed point does not exceed half the given angular threshold in either direction (in radians).  ARGS: (Vector3)point, (float)angle.
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None):
        pass

    @property
    def angle(self):
        """
        Angle.
        """

    @angle.setter
    def angle(self, value):
        """
        Angle.
        """

    @property
    def invert(self):
        """
        Invert.
        """

    @invert.setter
    def invert(self, value):
        """
        Invert.
        """

    def range(self, arg0):
        """
        Gets the interval at the specified point.  ARGS: (Vector3)point
        """

    def set_params(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        Sets Params for scoring function.  Points are scored by measuring distance from line formed by initial point and angle, then normalized to [0,1] where distance < ideal_distance is scored as 1, ideal_distance < distance < max_distance is scored as 1->0, and distance >= max_distance is scored as 0.  ARGS: (Vector3)point1, (Vector3)point2, (float)ideal_distance, (float)max_distance
        """

    @property
    def target(self):
        """
        Target Point.
        """

    @target.setter
    def target(self, value):
        """
        Target Point.
        """


class RelativeFacingWithCircle():
    """
    A restriction on facing a fixed point, with arbitrary facing allowed within a circle of given radius.
    ARGS: (Vector3)point, (float)angle (float)radius.
    """

    def __init__(self):
        pass

    @property
    def angle(self):
        """
        Angle.
        """

    @angle.setter
    def angle(self, value):
        """
        Angle.
        """

    @property
    def radius(self):
        """
        Target Point.
        """

    @radius.setter
    def radius(self, value):
        """
        Target Point.
        """

    def range(self, arg0):
        """
        Gets the interval at the specified point.  ARGS: (Vector3)point
        """

    def set_params(self, arg0, arg1, arg2):
        """
        Sets Params for scoring function.  Points are scored by measuring distance from line formed by initial point and angle, then normalized to [0,1] where distance < ideal_distance is scored as 1, ideal_distance < distance < max_distance is scored as 1->0, and distance >= max_distance is scored as 0.  ARGS: (Vector3)point1, (Vector3)point2, (float)ideal_distance, (float)max_distance
        """

    @property
    def target(self):
        """
        Target Point.
        """

    @target.setter
    def target(self, value):
        """
        Target Point.
        """


def angular_weighted_average(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None):
    """
    Compute the weighted average of angles a and b.
    The return value is not normalized in the range [0, 2 * Pi).
    There are two possible orientations, depending on whether we
    consider the clockwise or counterclockwise arc.  The smaller arc
    is used (if they are the same, use the arc from a to b).
    """


def find_intersection_points(arg0, arg1, arg2, arg3, arg4, arg5):
    """
    Given a line segment, find all rays that intersect with it and return the points of intersection
    """


def generate_circle_constraint(arg0, arg1, arg2):
    """
    (num_sides: int, center: Vector3, radius: float) -> Polygon
    Generate a Circular Polygon used by the Python constraint system.
    """


def generate_cone_constraint(arg0, arg1, arg2, arg3, arg4, arg5, arg6):
    """
    (target_pos: Vector3, target_facing: Vector3, min_dist: float
    , max_dist: float, angle: float, offset: float) -> Polygon
    Generate a Cone Polygon used by the Python constraint system.
    """


def interval_from_facing_angle(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
    """
    Return an angular interval constructed from a given facing and angular width.
    """
