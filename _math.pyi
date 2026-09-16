# Annotations Created by TURBODRIVER

"""
Optimized math implementations
"""

from typing import *

import _pathing

class CircularUtilityCurve():
    """
    A piecewise linear curve with min & max values for X that wrap.
    """

    def __init__(self, points: 'Sequence[Tuple[float, float]]', min_x: 'float' = 0.0, max_x: 'float' = 1.0):
        """
        A piecewise linear curve with min & max values for X that wrap.
        """

    def get(self, val: 'float') -> 'float':
        pass


class LinearCurve():
    """
    A curve described by a series of points with linear interpolation between them.    If two points share the same X axis value, the last point in the list will take precedence.    This means that LinearCurves are directional, in that the closed edge of two adjacent discontinuous    intervals is the last point at that X value.
    """

    def __init__(self, points: 'Sequence[Tuple[float, float]]'):
        """
        A curve described by a series of points with linear interpolation between them.    If two points share the same X axis value, the last point in the list will take precedence.    This means that LinearCurves are directional, in that the closed edge of two adjacent discontinuous    intervals is the last point at that X value.
        """

    def get(self, val: 'float') -> 'float':
        pass


class Location():
    """
    Location(Transform, RoutingSurface, Parent, JointNameOrHash, SlotName)
    """

    def __init__(self, transform: 'Optional[Transform]' = None, routing_surface: 'Optional[_pathing.SurfaceIdentifier]' = None, parent: 'Optional[Any]' = None, joint_name_or_hash: 'Optional[Union[str, int]]' = None, slot_hash: 'int' = 0):
        """
        Location(Transform, RoutingSurface, Parent, JointNameOrHash, SlotName)
        """

    def clone(self, transform: 'Optional[Transform]' = None, routing_surface: 'Optional[_pathing.SurfaceIdentifier]' = None, parent: 'Optional[Any]' = None, joint_name_or_hash: 'Optional[Union[str, int]]' = None, slot_hash: 'Optional[int]' = None) -> 'Location':
        pass

    def duplicate(self) -> 'Location':
        pass

    @property
    def joint_name_hash(self) -> 'int':
        pass

    @joint_name_hash.setter
    def joint_name_hash(self, value: 'int'):
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
    def parent(self) -> 'Optional[Any]':
        pass

    @parent.setter
    def parent(self, value: 'Optional[Any]'):
        pass

    @property
    def routing_surface(self) -> '_pathing.SurfaceIdentifier':
        pass

    @routing_surface.setter
    def routing_surface(self, value: '_pathing.SurfaceIdentifier'):
        pass

    @property
    def slot_hash(self) -> 'int':
        pass

    @slot_hash.setter
    def slot_hash(self, value: 'int'):
        pass

    @property
    def transform(self) -> 'Transform':
        pass

    @transform.setter
    def transform(self, value: 'Transform'):
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

    def __init__(self, x: 'float' = 0.0, y: 'float' = 0.0, z: 'float' = 0.0, w: 'float' = 1.0):
        """
        Quaternion(x, y, z, w)
        """

    @staticmethod
    def IDENTITY(self) -> 'Quaternion':
        pass

    @staticmethod
    def ZERO(self) -> 'Quaternion':
        pass

    def __getitem__(self, key: 'int') -> 'float':
        """
        Return self[key].
        """

    @staticmethod
    def concatenate(self, q1: 'Quaternion', q2: 'Quaternion') -> 'Quaternion':
        pass

    @staticmethod
    def from_axis_angle(self, angle: 'float', vector: '_math.Vector3') -> 'Quaternion':
        """
        from_axis_angle(angle, vector) -> Quaternion
        
        Construct a quaternion from a give angle and axis of rotation.
        """

    @staticmethod
    def from_forward_vector(self, vector: '_math.Vector3') -> 'Quaternion':
        """
        from_forward_vector(vector) -> Quaternion
        
        Construct a quaternion from a forward vector
        """

    @staticmethod
    def transform_vector(self, q: 'Quaternion', v: '_math.Vector3') -> '_math.Vector3':
        """
        transform_vector(v) -> Vector3
        
        Transform a Vector3 by this Quaternion.
        """

    @property
    def w(self) -> 'float':
        pass

    @w.setter
    def w(self, value: 'float'):
        pass

    @property
    def x(self) -> 'float':
        pass

    @x.setter
    def x(self, value: 'float'):
        pass

    @property
    def y(self) -> 'float':
        pass

    @y.setter
    def y(self, value: 'float'):
        pass

    @property
    def z(self) -> 'float':
        pass

    @z.setter
    def z(self, value: 'float'):
        pass


class QuaternionImmutable(Quaternion):
    """
    QuaternionImmutable(x, y, z, w)
    """

    def __init__(self, x: 'float' = 0.0, y: 'float' = 0.0, z: 'float' = 0.0, w: 'float' = 1.0):
        """
        QuaternionImmutable(x, y, z, w)
        """

    @staticmethod
    def IDENTITY(self) -> 'QuaternionImmutable':
        pass

    @staticmethod
    def ZERO(self) -> 'QuaternionImmutable':
        pass

    def __getitem__(self, key: 'int') -> 'float':
        """
        Return self[key].
        """

    @staticmethod
    def concatenate(self, q1: 'Union[Quaternion, QuaternionImmutable]', q2: 'Union[Quaternion, QuaternionImmutable]') -> 'QuaternionImmutable':
        pass

    @staticmethod
    def from_axis_angle(self, angle: 'float', vector: '_math.Vector3') -> 'QuaternionImmutable':
        """
        from_axis_angle(angle, vector) -> Quaternion
        
        Construct a quaternion from a give angle and axis of rotation.
        """

    @staticmethod
    def from_forward_vector(self, vector: '_math.Vector3') -> 'QuaternionImmutable':
        """
        from_forward_vector(vector) -> Quaternion
        
        Construct a quaternion from a forward vector
        """

    @staticmethod
    def transform_vector(self, q: 'Quaternion', v: '_math.Vector3') -> '_math.Vector3':
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

    def __init__(self, translation: 'Optional[Vector3]' = None, orientation: 'Optional[Quaternion]' = None):
        """
        Transform(Vector3(x, y, z), Quaternion(x, y, z, w))
        """

    @staticmethod
    def IDENTITY(self) -> 'Transform':
        pass

    @staticmethod
    def ZERO(self) -> 'Transform':
        pass

    @staticmethod
    def concatenate(self, t1: 'Transform', t2: 'Transform') -> 'Transform':
        pass

    @property
    def orientation(self) -> 'Quaternion':
        pass

    @orientation.setter
    def orientation(self, value: 'Quaternion'):
        pass

    def transform_point(self, v) -> 'Vector3':
        """
        transform_point(v) -> Vector3
        
        Transforms a Vector3 by this Transform's elements.
        """

    def transform_vector(self, v) -> 'Vector3':
        """
        transform_vector(v) -> Vector3
        
        Transform a Vector3 by this Transform's Quaternion element.
        """

    @property
    def translation(self) -> 'Vector3':
        pass

    @translation.setter
    def translation(self, value: 'Vector3'):
        pass


class Vector2():
    """
    Vector2(x, y)
    """

    def __init__(self, x: 'float' = 0.0, y: 'float' = 0.0):
        """
        Vector2(x, y)
        """

    @staticmethod
    def ONE(self) -> 'Vector2':
        pass

    @staticmethod
    def X_AXIS(self) -> 'Vector2':
        pass

    @staticmethod
    def Y_AXIS(self) -> 'Vector2':
        pass

    @staticmethod
    def ZERO(self) -> 'Vector2':
        pass

    def __abs__(self) -> 'float':
        """
        abs(self)
        """

    def __add__(self, value: 'Union[Vector2, float]') -> 'Vector2':
        """
        Return self+value.
        """

    def __bool__(self) -> 'bool':
        """
        self != 0
        """

    def __getitem__(self, key: 'int') -> 'float':
        """
        Return self[key].
        """

    def __iadd__(self, value: 'Union[Vector2, float]') -> 'Vector2':
        """
        Return self+=value.
        """

    def __imul__(self, value: 'Union[Vector2, float]') -> 'Vector2':
        """
        Return self*=value.
        """

    def __isub__(self, value: 'Union[Vector2, float]') -> 'Vector2':
        """
        Return self-=value.
        """

    def __itruediv__(self, value: 'Union[Vector2, float]') -> 'Vector2':
        """
        Return self/=value.
        """

    def __len__(self) -> 'int':
        """
        Return len(self).
        """

    def __mul__(self, value: 'Union[Vector2, float]') -> 'Vector2':
        """
        Return self*value.
        """

    def __neg__(self) -> 'Vector2':
        """
        -self
        """

    def __radd__(self, value: 'Union[Vector2, float]') -> 'Vector2':
        """
        Return value+self.
        """

    def __rmul__(self, value: 'Union[Vector2, float]') -> 'Vector2':
        """
        Return value*self.
        """

    def __rsub__(self, value: 'Union[Vector2, float]') -> 'Vector2':
        """
        Return value-self.
        """

    def __rtruediv__(self, value: 'Union[Vector2, float]') -> 'Vector2':
        """
        Return value/self.
        """

    def __sub__(self, value: 'Union[Vector2, float]') -> 'Vector2':
        """
        Return self-value.
        """

    def __truediv__(self, value: 'Union[Vector2, float]') -> 'Vector2':
        """
        Return self/value.
        """

    def magnitude(self) -> 'float':
        """
        Return the magnitude (length) of this vector.
        For faster execution, use magnitude_squared.
        """

    def magnitude_squared(self) -> 'float':
        """
        Return squared value of the magnitude (length) of this vector.
        """

    @property
    def x(self) -> 'float':
        pass

    @x.setter
    def x(self, value: 'float'):
        pass

    @property
    def y(self) -> 'float':
        pass

    @y.setter
    def y(self, value: 'float'):
        pass


class Vector3():
    """
    Vector3(x, y, z)
    """

    def __init__(self, x: 'float' = 0.0, y: 'float' = 0.0, z: 'float' = 0.0):
        """
        Vector3(x, y, z)
        """

    @staticmethod
    def ONE(self) -> 'Vector3':
        pass

    @staticmethod
    def X_AXIS(self) -> 'Vector3':
        pass

    @staticmethod
    def Y_AXIS(self) -> 'Vector3':
        pass

    @staticmethod
    def ZERO(self) -> 'Vector3':
        pass

    @staticmethod
    def Z_AXIS(self) -> 'Vector3':
        pass

    def __abs__(self) -> 'float':
        """
        abs(self)
        """

    def __add__(self, value: 'Union[Vector3, float]') -> 'Vector3':
        """
        Return self+value.
        """

    def __bool__(self) -> 'bool':
        """
        self != 0
        """

    def __getitem__(self, key: 'int') -> 'float':
        """
        Return self[key].
        """

    def __iadd__(self, value: 'Union[Vector3, float]') -> 'Vector3':
        """
        Return self+=value.
        """

    def __imul__(self, value: 'Union[Vector3, float]') -> 'Vector3':
        """
        Return self*=value.
        """

    def __isub__(self, value: 'Union[Vector3, float]') -> 'Vector3':
        """
        Return self-=value.
        """

    def __itruediv__(self, value: 'Union[Vector3, float]') -> 'Vector3':
        """
        Return self/=value.
        """

    def __len__(self) -> 'int':
        """
        Return len(self).
        """

    def __mul__(self, value: 'Union[Vector3, float]') -> 'Vector3':
        """
        Return self*value.
        """

    def __neg__(self) -> 'Vector3':
        """
        -self
        """

    def __radd__(self, value: 'Union[Vector3, float]') -> 'Vector3':
        """
        Return value+self.
        """

    def __rmul__(self, value: 'Union[Vector3, float]') -> 'Vector3':
        """
        Return value*self.
        """

    def __rsub__(self, value: 'Union[Vector3, float]') -> 'Vector3':
        """
        Return value-self.
        """

    def __rtruediv__(self, value: 'Union[Vector3, float]') -> 'Vector3':
        """
        Return value/self.
        """

    def __sub__(self, value: 'Union[Vector3, float]') -> 'Vector3':
        """
        Return self-value.
        """

    def __truediv__(self, value: 'Union[Vector3, float]') -> 'Vector3':
        """
        Return self/value.
        """

    def magnitude(self) -> 'float':
        """
        Return the magnitude (length) of this vector.
        For faster execution, use magnitude_squared.
        """

    def magnitude_2d(self) -> 'float':
        """
        Return the magnitude (length) of this vector's X and Z components.
        For faster execution, use magnitude_2d_squared.
        """

    def magnitude_2d_squared(self) -> 'float':
        """
        Return squared value of the magnitude (length) of this vector's X and Z components.
        """

    def magnitude_squared(self) -> 'float':
        """
        Return squared value of the magnitude (length) of this vector.
        """

    @property
    def x(self) -> 'float':
        pass

    @x.setter
    def x(self, value: 'float'):
        pass

    @property
    def y(self) -> 'float':
        pass

    @y.setter
    def y(self, value: 'float'):
        pass

    @property
    def z(self) -> 'float':
        pass

    @z.setter
    def z(self, value: 'float'):
        pass


class Vector3Immutable(Vector3):
    """
    Vector3Immutable(x, y, z)
    """

    def __init__(self, x: 'float' = 0.0, y: 'float' = 0.0, z: 'float' = 0.0):
        """
        Vector3Immutable(x, y, z)
        """

    @staticmethod
    def ONE(self) -> 'Vector3Immutable':
        pass

    @staticmethod
    def X_AXIS(self) -> 'Vector3Immutable':
        pass

    @staticmethod
    def Y_AXIS(self) -> 'Vector3Immutable':
        pass

    @staticmethod
    def ZERO(self) -> 'Vector3Immutable':
        pass

    @staticmethod
    def Z_AXIS(self) -> 'Vector3Immutable':
        pass

    def __abs__(self) -> 'float':
        """
        abs(self)
        """

    def __add__(self, value: 'Union[Vector3Immutable, Vector3, float]') -> 'Vector3Immutable':
        """
        Return self+value.
        """

    def __bool__(self) -> 'bool':
        """
        self != 0
        """

    def __getitem__(self, key: 'int') -> 'float':
        """
        Return self[key].
        """

    def __iadd__(self, value: 'Union[Vector3Immutable, Vector3, float]') -> 'Vector3Immutable':
        """
        Return self+=value.
        """

    def __imul__(self, value: 'Union[Vector3Immutable, Vector3, float]') -> 'Vector3Immutable':
        """
        Return self*=value.
        """

    def __isub__(self, value: 'Union[Vector3Immutable, Vector3, float]') -> 'Vector3Immutable':
        """
        Return self-=value.
        """

    def __itruediv__(self, value: 'Union[Vector3Immutable, Vector3, float]') -> 'Vector3Immutable':
        """
        Return self/=value.
        """

    def __len__(self) -> 'int':
        """
        Return len(self).
        """

    def __mul__(self, value: 'Union[Vector3Immutable, Vector3, float]') -> 'Vector3Immutable':
        """
        Return self*value.
        """

    def __neg__(self) -> 'Vector3Immutable':
        """
        -self
        """

    def __radd__(self, value: 'Union[Vector3Immutable, Vector3, float]') -> 'Vector3Immutable':
        """
        Return value+self.
        """

    def __rmul__(self, value: 'Union[Vector3Immutable, Vector3, float]') -> 'Vector3Immutable':
        """
        Return value*self.
        """

    def __rsub__(self, value: 'Union[Vector3Immutable, Vector3, float]') -> 'Vector3Immutable':
        """
        Return value-self.
        """

    def __rtruediv__(self, value: 'Union[Vector3Immutable, Vector3, float]') -> 'Vector3Immutable':
        """
        Return value/self.
        """

    def __sub__(self, value: 'Union[Vector3Immutable, Vector3, float]') -> 'Vector3Immutable':
        """
        Return self-value.
        """

    def __truediv__(self, value: 'Union[Vector3Immutable, Vector3, float]') -> 'Vector3Immutable':
        """
        Return self/value.
        """

    def magnitude(self) -> 'float':
        """
        Return the magnitude (length) of this vector.
        For faster execution, use magnitude_squared.
        """

    def magnitude_2d(self) -> 'float':
        """
        Return the magnitude (length) of this vector's X and Z components.
        For faster execution, use magnitude_2d_squared.
        """

    def magnitude_2d_squared(self) -> 'float':
        """
        Return squared value of the magnitude (length) of this vector's X and Z components.
        """

    def magnitude_squared(self) -> 'float':
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

    def __init__(self, points: 'Sequence[Tuple[float, float]]', max_y: 'float' = 0.0, weight: 'float' = 1.0):
        """
        A curve that normalizes the results of a linear curve.
        """

    def get(self, val: 'float') -> 'float':
        pass


def minimum_distance(v1: 'Vector3', v2: 'Vector3') -> 'float':
    """
    Given a source point, and a series of points, return the distance to the closest point in the series
    """


def mod_2pi(angle: 'float') -> 'float':
    """
    Given a float value, will return fmod(value, 2*PI)
    """
