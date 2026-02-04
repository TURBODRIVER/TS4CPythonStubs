"""
Kingdom Utilities
"""

from typing import *


class KingdomNeighborhood():
    """
    KingdomNeighborhood
    """

    def __init__(self, kwarg0: Any = None):
        pass

    def get_as_pb(self, arg0):
        """
        Gets the KingdomNeighborhood as a KingdomNeighborhoodData protobuf.
        """

    @property
    def neighborhood_id(self):
        """
        Neighborhood ID
        """

    @neighborhood_id.setter
    def neighborhood_id(self, value):
        """
        Neighborhood ID
        """

    def set_from_pb(self, arg0):
        """
        Sets the KingdomNeighborhood from KingdomNeighborhoodData protobuf.
        """

    @property
    def sims(self):
        """
        List of Sims in the neighborhood.
        """

    @sims.setter
    def sims(self, value):
        """
        List of Sims in the neighborhood.
        """


class KingdomSim():
    """
    KingdomSim
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None):
        pass

    def get_as_pb(self, arg0):
        """
        Gets the KingdomSim as a KingdomSimData protobuf.
        """

    @property
    def inheriting_sim_id(self):
        """
        Inheriting Sim Id
        """

    @inheriting_sim_id.setter
    def inheriting_sim_id(self, value):
        """
        Inheriting Sim Id
        """

    @property
    def level(self):
        """
        Sim level
        """

    @level.setter
    def level(self, value):
        """
        Sim level
        """

    @property
    def priority(self):
        """
        Sim Priority
        """

    @priority.setter
    def priority(self, value):
        """
        Sim Priority
        """

    def set_from_pb(self, arg0):
        """
        Sets the KingdomSim from KingdomSimData protobuf.
        """

    @property
    def sim_id(self):
        """
        Sim Id
        """

    @sim_id.setter
    def sim_id(self, value):
        """
        Sim Id
        """


def refresh_sims(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
    """
    Refresh sim data
    """


def sim_death_or_abdicate(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None):
    """
    Remove a sim from the Kingdom because they died or abdicated.
    """


def sim_rejoined(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None):
    """
    Re-add a sim to the Kingdom as Tertiary. Requires a Primary parent.
    """
