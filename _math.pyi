"""
Optimized math implementations
"""

from typing import *


class CircularUtilityCurve():
    """
    A piecewise linear curve with min & max values for X that wrap.
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
        pass

    def get(self):
        pass


class LinearCurve():
    """
    A curve described by a series of points with linear interpolation between them.    If two points share the same X axis value, the last point in the list will take precedence.    This means that LinearCurves are directional, in that the closed edge of two adjacent discontinuous    intervals is the last point at that X value.
    """

    def __init__(self, kwarg0: Any = None):
        pass

    def get(self):
        pass


class Location():
    """
    Location(Transform, RoutingSurface, Parent, JointNameOrHash, SlotName)
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
        pass

    def clone(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None, kwarg5: Any = None, kwarg6: Any = None):
        pass

    def duplicate(self):
        pass

    @property
    def joint_name_hash(self):
        pass

    @joint_name_hash.setter
    def joint_name_hash(self, value):
        pass

    @property
    def joint_name_or_hash(self):
        pass

    @joint_name_or_hash.setter
    def joint_name_or_hash(self, value):
        pass

    @property
    def level(self):
        pass

    @level.setter
    def level(self, value):
        pass

    @property
    def parent(self):
        pass

    @parent.setter
    def parent(self, value):
        pass

    @property
    def routing_surface(self):
        pass

    @routing_surface.setter
    def routing_surface(self, value):
        pass

    @property
    def slot_hash(self):
        pass

    @slot_hash.setter
    def slot_hash(self, value):
        pass

    @property
    def transform(self):
        pass

    @transform.setter
    def transform(self, value):
        pass

    @property
    def world_routing_surface(self):
        pass

    @world_routing_surface.setter
    def world_routing_surface(self, value):
        pass

    @property
    def world_transform(self):
        pass

    @world_transform.setter
    def world_transform(self, value):
        pass

    @property
    def zone_id(self):
        pass

    @zone_id.setter
    def zone_id(self, value):
        pass


class Quaternion():
    """
    Quaternion(x, y, z, w)
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None):
        pass

    def IDENTITY(self):
        pass

    def ZERO(self):
        pass

    def __getitem__(self):
        """
        Return self[key].
        """

    def concatenate(self, arg0, arg1):
        pass

    def from_axis_angle(self, angle, vector) -> "Quaternion":
        """
        from_axis_angle(angle, vector) -> Quaternion
        
        Construct a quaternion from a give angle and axis of rotation.
        """

    def from_forward_vector(self, vector) -> "Quaternion":
        """
        from_forward_vector(vector) -> Quaternion
        
        Construct a quaternion from a forward vector
        """

    def transform_vector(self, v) -> "Vector3":
        """
        transform_vector(v) -> Vector3
        
        Transform a Vector3 by this Quaternion.
        """

    @property
    def w(self):
        pass

    @w.setter
    def w(self, value):
        pass

    @property
    def x(self):
        pass

    @x.setter
    def x(self, value):
        pass

    @property
    def y(self):
        pass

    @y.setter
    def y(self, value):
        pass

    @property
    def z(self):
        pass

    @z.setter
    def z(self, value):
        pass


class QuaternionImmutable():
    """
    QuaternionImmutable(x, y, z, w)
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None):
        pass

    def IDENTITY(self):
        pass

    def ZERO(self):
        pass

    def __getitem__(self):
        """
        Return self[key].
        """

    def concatenate(self, arg0, arg1):
        pass

    def from_axis_angle(self, angle, vector) -> "Quaternion":
        """
        from_axis_angle(angle, vector) -> Quaternion
        
        Construct a quaternion from a give angle and axis of rotation.
        """

    def from_forward_vector(self, vector) -> "Quaternion":
        """
        from_forward_vector(vector) -> Quaternion
        
        Construct a quaternion from a forward vector
        """

    def transform_vector(self, v) -> "Vector3":
        """
        transform_vector(v) -> Vector3
        
        Transform a Vector3 by this Quaternion.
        """

    @property
    def w(self):
        pass

    @w.setter
    def w(self, value):
        pass

    @property
    def x(self):
        pass

    @x.setter
    def x(self, value):
        pass

    @property
    def y(self):
        pass

    @y.setter
    def y(self, value):
        pass

    @property
    def z(self):
        pass

    @z.setter
    def z(self, value):
        pass


class Transform():
    """
    Transform(Vector3(x, y, z), Quaternion(x, y, z, w))
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None):
        pass

    def IDENTITY(self):
        pass

    def ZERO(self):
        pass

    def concatenate(self, arg0, arg1):
        pass

    @property
    def orientation(self):
        pass

    @orientation.setter
    def orientation(self, value):
        pass

    def transform_point(self, v) -> "Vector3":
        """
        transform_point(v) -> Vector3
        
        Transforms a Vector3 by this Transform's elements.
        """

    def transform_vector(self, v) -> "Vector3":
        """
        transform_vector(v) -> Vector3
        
        Transform a Vector3 by this Transform's Quaternion element.
        """

    @property
    def translation(self):
        pass

    @translation.setter
    def translation(self, value):
        pass


class Vector2():
    """
    Vector2(x, y)
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None):
        pass

    def ONE(self):
        pass

    def X_AXIS(self):
        pass

    def Y_AXIS(self):
        pass

    def ZERO(self):
        pass

    def __abs__(self):
        """
        abs(self)
        """

    def __add__(self):
        """
        Return self+value.
        """

    def __bool__(self):
        """
        self != 0
        """

    def __getitem__(self):
        """
        Return self[key].
        """

    def __iadd__(self):
        """
        Return self+=value.
        """

    def __imul__(self):
        """
        Return self*=value.
        """

    def __isub__(self):
        """
        Return self-=value.
        """

    def __itruediv__(self):
        """
        Return self/=value.
        """

    def __len__(self):
        """
        Return len(self).
        """

    def __mul__(self):
        """
        Return self*value.
        """

    def __neg__(self):
        """
        -self
        """

    def __radd__(self):
        """
        Return value+self.
        """

    def __rmul__(self):
        """
        Return value*self.
        """

    def __rsub__(self):
        """
        Return value-self.
        """

    def __rtruediv__(self):
        """
        Return value/self.
        """

    def __sub__(self):
        """
        Return self-value.
        """

    def __truediv__(self):
        """
        Return self/value.
        """

    def magnitude(self):
        """
        Return the magnitude (length) of this vector.
        For faster execution, use magnitude_squared.
        """

    def magnitude_squared(self):
        """
        Return squared value of the magnitude (length) of this vector.
        """

    @property
    def x(self):
        pass

    @x.setter
    def x(self, value):
        pass

    @property
    def y(self):
        pass

    @y.setter
    def y(self, value):
        pass


class Vector3():
    """
    Vector3(x, y, z)
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
        pass

    def ONE(self):
        pass

    def X_AXIS(self):
        pass

    def Y_AXIS(self):
        pass

    def ZERO(self):
        pass

    def Z_AXIS(self):
        pass

    def __abs__(self):
        """
        abs(self)
        """

    def __add__(self):
        """
        Return self+value.
        """

    def __bool__(self):
        """
        self != 0
        """

    def __getitem__(self):
        """
        Return self[key].
        """

    def __iadd__(self):
        """
        Return self+=value.
        """

    def __imul__(self):
        """
        Return self*=value.
        """

    def __isub__(self):
        """
        Return self-=value.
        """

    def __itruediv__(self):
        """
        Return self/=value.
        """

    def __len__(self):
        """
        Return len(self).
        """

    def __mul__(self):
        """
        Return self*value.
        """

    def __neg__(self):
        """
        -self
        """

    def __radd__(self):
        """
        Return value+self.
        """

    def __rmul__(self):
        """
        Return value*self.
        """

    def __rsub__(self):
        """
        Return value-self.
        """

    def __rtruediv__(self):
        """
        Return value/self.
        """

    def __sub__(self):
        """
        Return self-value.
        """

    def __truediv__(self):
        """
        Return self/value.
        """

    def magnitude(self):
        """
        Return the magnitude (length) of this vector.
        For faster execution, use magnitude_squared.
        """

    def magnitude_2d(self):
        """
        Return the magnitude (length) of this vector's X and Z components.
        For faster execution, use magnitude_2d_squared.
        """

    def magnitude_2d_squared(self):
        """
        Return squared value of the magnitude (length) of this vector's X and Z components.
        """

    def magnitude_squared(self):
        """
        Return squared value of the magnitude (length) of this vector.
        """

    @property
    def x(self):
        pass

    @x.setter
    def x(self, value):
        pass

    @property
    def y(self):
        pass

    @y.setter
    def y(self, value):
        pass

    @property
    def z(self):
        pass

    @z.setter
    def z(self, value):
        pass


class Vector3Immutable():
    """
    Vector3Immutable(x, y, z)
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
        pass

    def ONE(self):
        pass

    def X_AXIS(self):
        pass

    def Y_AXIS(self):
        pass

    def ZERO(self):
        pass

    def Z_AXIS(self):
        pass

    def __abs__(self):
        """
        abs(self)
        """

    def __add__(self):
        """
        Return self+value.
        """

    def __bool__(self):
        """
        self != 0
        """

    def __getitem__(self):
        """
        Return self[key].
        """

    def __iadd__(self):
        """
        Return self+=value.
        """

    def __imul__(self):
        """
        Return self*=value.
        """

    def __isub__(self):
        """
        Return self-=value.
        """

    def __itruediv__(self):
        """
        Return self/=value.
        """

    def __len__(self):
        """
        Return len(self).
        """

    def __mul__(self):
        """
        Return self*value.
        """

    def __neg__(self):
        """
        -self
        """

    def __radd__(self):
        """
        Return value+self.
        """

    def __rmul__(self):
        """
        Return value*self.
        """

    def __rsub__(self):
        """
        Return value-self.
        """

    def __rtruediv__(self):
        """
        Return value/self.
        """

    def __sub__(self):
        """
        Return self-value.
        """

    def __truediv__(self):
        """
        Return self/value.
        """

    def magnitude(self):
        """
        Return the magnitude (length) of this vector.
        For faster execution, use magnitude_squared.
        """

    def magnitude_2d(self):
        """
        Return the magnitude (length) of this vector's X and Z components.
        For faster execution, use magnitude_2d_squared.
        """

    def magnitude_2d_squared(self):
        """
        Return squared value of the magnitude (length) of this vector's X and Z components.
        """

    def magnitude_squared(self):
        """
        Return squared value of the magnitude (length) of this vector.
        """

    @property
    def x(self):
        pass

    @x.setter
    def x(self, value):
        pass

    @property
    def y(self):
        pass

    @y.setter
    def y(self, value):
        pass

    @property
    def z(self):
        pass

    @z.setter
    def z(self, value):
        pass


class WeightedUtilityCurve():
    """
    A curve that normalizes the results of a linear curve.
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None):
        pass

    def get(self):
        pass


def minimum_distance(arg0, arg1):
    """
    Given a source point, and a series of points, return the distance to the closest point in the series
    """


def mod_2pi(value):
    """
    Given a float value, will return fmod(value, 2*PI)
    """
