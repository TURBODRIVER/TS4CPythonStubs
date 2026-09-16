# Annotations Created by TURBODRIVER

"""
Kingdom Utilities
"""

from typing import *

import protocolbuffers.Kingdom_pb2

class KingdomNeighborhood():
    """
    KingdomNeighborhood
    """

    def __init__(self, neighborhood_id: 'int' = 0):
        """
        KingdomNeighborhood
        """

    def get_as_pb(self, pb_data: 'protocolbuffers.Kingdom_pb2.KingdomNeighborhoodData'):
        """
        Gets the KingdomNeighborhood as a KingdomNeighborhoodData protobuf.
        """

    @property
    def neighborhood_id(self) -> 'int':
        """
        Neighborhood ID
        """

    @neighborhood_id.setter
    def neighborhood_id(self, value: 'int'):
        """
        Neighborhood ID
        """

    def set_from_pb(self, pb_data: 'protocolbuffers.Kingdom_pb2.KingdomNeighborhoodData'):
        """
        Sets the KingdomNeighborhood from KingdomNeighborhoodData protobuf.
        """

    @property
    def sims(self) -> 'List[KingdomSim]':
        """
        List of Sims in the neighborhood.
        """

    @sims.setter
    def sims(self, value: 'List[KingdomSim]'):
        """
        List of Sims in the neighborhood.
        """


class KingdomSim():
    """
    KingdomSim
    """

    def __init__(self, sim_id: 'int' = 0, level: 'int' = 0, priority: 'int' = 0, inheriting_sim_id: 'int' = 0):
        """
        KingdomSim
        """

    def get_as_pb(self, pb_data: 'protocolbuffers.Kingdom_pb2.KingdomSimData'):
        """
        Gets the KingdomSim as a KingdomSimData protobuf.
        """

    @property
    def inheriting_sim_id(self) -> 'int':
        """
        Inheriting Sim Id
        """

    @inheriting_sim_id.setter
    def inheriting_sim_id(self, value: 'int'):
        """
        Inheriting Sim Id
        """

    @property
    def level(self) -> 'int':
        """
        Sim level
        """

    @level.setter
    def level(self, value: 'int'):
        """
        Sim level
        """

    @property
    def priority(self) -> 'int':
        """
        Sim Priority
        """

    @priority.setter
    def priority(self, value: 'int'):
        """
        Sim Priority
        """

    def set_from_pb(self, pb_data: 'protocolbuffers.Kingdom_pb2.KingdomSimData'):
        """
        Sets the KingdomSim from KingdomSimData protobuf.
        """

    @property
    def sim_id(self) -> 'int':
        """
        Sim Id
        """

    @sim_id.setter
    def sim_id(self, value: 'int'):
        """
        Sim Id
        """


def refresh_sims(family: 'List[Dict[str, Union[int, List[int]]]]', affected_sim_ids: 'List[int]', neighborhood_data: 'KingdomNeighborhood') -> 'List[KingdomNeighborhood]':
    """
    Refresh sim data
    """


def sim_death_or_abdicate(family: 'List[Dict[str, Union[int, List[int]]]]', affected_sim_ids: 'List[int]', neighborhood_data: 'KingdomNeighborhood', dead_sim_id: 'int') -> 'Tuple[List[KingdomNeighborhood], int]':
    """
    Remove a sim from the Kingdom because they died or abdicated.
    """


def sim_rejoined(family: 'List[Dict[str, Union[int, List[int]]]]', affected_sim_ids: 'List[int]', neighborhood_data: 'KingdomNeighborhood', rejoined_sim_id: 'int') -> 'List[KingdomNeighborhood]':
    """
    Re-add a sim to the Kingdom as Tertiary. Requires a Primary parent.
    """
