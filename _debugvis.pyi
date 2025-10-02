"""
Interface to server debug visualization layers
"""


class Layer():
    """
    Layer() -> New debug visualization layer.
    """

    def __init__(self):
        pass

    def add_point(self, p, size=0.1, color=None) -> "Add point a location p to an open layer":
        """
        -> Add point a location p to an open layer
        """

    def add_segment(self, a, b, color=None) -> "Add a segment between a and b to an open layer":
        """
        -> Add a segment between a and b to an open layer
        """

    def add_text_object(self, obj_id, text, bone_index=0, offset=None, color_foreground=None, color_background=None) -> "Add text relative to the position of the given object to an open layer":
        """
        -> Add text relative to the position of the given object to an open layer
        """

    def add_text_screen(self, p, text, color_foreground=None, color_background=None) -> "Add text at screen coordinates p to an open layer":
        """
        -> Add text at screen coordinates p to an open layer
        """

    def add_text_world(self, p, text, color_foreground=None, color_background=None) -> "Add text at world coordinates p to an open layer":
        """
        -> Add text at world coordinates p to an open layer
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


def get_layer(name) -> "New or existing layer with given name":
    """
    -> New or existing layer with given name
    """
