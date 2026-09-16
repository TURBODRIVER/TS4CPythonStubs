# Annotations Created by TURBODRIVER

"""
Interface to server debug visualization layers
"""

from typing import *

import _math

class Layer():
    """
    Layer() -> New debug visualization layer.
    """

    def __init__(self):
        """
        Layer() -> New debug visualization layer.
        """

    def add_point(self, p: '_math.Vector3', size: 'float' = 0.1, color: 'Optional[int]' = None):
        """
        add_point(p, size=0.1, color=None) -> Add point a location p to an open layer
        """

    def add_segment(self, a: '_math.Vector3', b: '_math.Vector3', color: 'Optional[int]' = None):
        """
        add_segment(a, b, color=None) -> Add a segment between a and b to an open layer
        """

    def add_text_object(self, obj_id: 'int', text: 'str', bone_index: 'int' = 0, offset: 'Optional[_math.Vector3]' = None, color_foreground: 'Optional[int]' = None, color_background: 'Optional[int]' = None):
        """
        add_text_object(obj_id, text, bone_index=0, offset=None, color_foreground=None, color_background=None) -> Add text relative to the position of the given object to an open layer
        """

    def add_text_screen(self, p: '_math.Vector2', text: 'str', color_foreground: 'Optional[int]' = None, color_background: 'Optional[int]' = None):
        """
        add_text_screen(p, text, color_foreground=None, color_background=None) -> Add text at screen coordinates p to an open layer
        """

    def add_text_world(self, p: '_math.Vector3', text: 'str', color_foreground: 'Optional[int]' = None, color_background: 'Optional[int]' = None):
        """
        add_text_world(p, text, color_foreground=None, color_background=None) -> Add text at world coordinates p to an open layer
        """

    def clear(self):
        """
        Clear an open layer
        """

    def commit(self):
        """
        Commit changes to an open layer and send to registered clients
        """

    def open(self):
        """
        Open a layer for modification
        """


def get_layer(name: 'str', zone_id: 'Optional[int]' = None) -> 'Layer':
    """
    get_layer(name) -> New or existing layer with given name
    """
