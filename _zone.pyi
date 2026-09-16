# Annotations Created by TURBODRIVER

"""
Zone Module.
"""

from typing import *

import _math

class Zone():
    """
    Describes the configuration of the active zone.
    """

    def __init__(self):
        """
        Describes the configuration of the active zone.
        """

    @property
    def active_lot_id(self) -> 'int':
        """
        The active lot id.
        """

    @active_lot_id.setter
    def active_lot_id(self, value: 'int'):
        """
        The active lot id.
        """

    @property
    def display_name_key(self) -> 'int':
        """
        The displayed name for the zone.
        """

    @display_name_key.setter
    def display_name_key(self, value: 'int'):
        """
        The displayed name for the zone.
        """

    @property
    def start_pos(self) -> '_math.Vector3':
        """
        The sim's starting position in the zone.
        """

    @start_pos.setter
    def start_pos(self, value: '_math.Vector3'):
        """
        The sim's starting position in the zone.
        """


def add_sim(sim_id: 'int', zone_id: 'int') -> 'bool':
    """
    Tell C++ that a Sim was created in the zone instance.
    """


def create_venue(household_id: 'int', venue_type: 'int', zone_id: 'int', lot_id: 'int', world_id: 'int') -> 'int':
    """
    Creates a venue from a household instance id and returns the zone instance id.
    """


def get_building_type(house_description_id: 'int') -> 'int':
    """
    Returns the building type from the house description provided.
    """


def get_eco_footprint_value(house_description_id: 'int') -> 'float':
    """
    Returns the default eco footprint value from the house description provided.
    """


def get_hide_from_lot_picker(lot_description_id: 'int', world_description_id: 'int') -> 'bool':
    """
    Checks if the given lot/world id pair is tuned in catalog side to be hidden from the lot picker UI.
    """


def get_house_description_id(lot_template_id: 'int', zone_id: 'Optional[int]' = None, world_id: 'Optional[int]' = None) -> 'int':
    """
    Returns the house description id from the lot template id provided.
    """


def get_is_eco_footprint_compatible_for_world_description(world_description_id: 'int') -> 'bool':
    """
    Given a world description id, return true if it is eco footprint compatible.
    """


def get_lot_description_id(lot_id: 'int', world_description_id: 'int') -> 'int':
    """
    Returns the lot description id from the lot's id.
    """


def get_rent(house_description_id: 'int') -> 'int':
    """
    Returns the rent amount set on the house description.
    """


def get_signed_lease_length(house_description_id: 'int') -> 'int':
    """
    Returns the lease length amount set on the house description.
    """


def get_world_and_lot_description_id_from_zone_id(zone_id: 'int') -> 'Tuple[int, int]':
    """
    Returns the tuple (world description id, lot description id from the zone id.
    """


def get_world_description_id(world_id: 'int') -> 'int':
    """
    Returns the world/street description id from the world's id.
    """


def get_world_id(world_description_id: 'int') -> 'int':
    """
    Returns the world id from the world description id.
    """


def has_entitlement(pack: 'int') -> 'bool':
    """
    Checks if the given account can use provided entitlement.
    """


def invite_sims_to_zone(sim_ids: 'Sequence[int]', zone_id: 'int') -> 'bool':
    """
    Requests a travel reservation for remote sims in order to try and pull them to the calling zone.
    """


def is_available_pack(pack: 'int') -> 'bool':
    """
    Return True if the the given account is entitled to the specified pack and it is installed on this machine. False otherwise.
    """


def is_displayable(pack: 'int') -> 'bool':
    """
    Checks if the entitlement is visible to the player, regardless if the player has the entitlement.
    """


def is_entitled_pack(pack: 'int') -> 'bool':
    """
    Return True if the given account is entitled to the specified pack. False otherwise.
    """


def is_event_enabled(event_id: 'int') -> 'bool':
    """
    Checks if the given event switch is enabled.
    """


def is_granted_or_non_account_reward_item(item_id: 'int', account_id: 'Optional[int]' = None) -> 'bool':
    """
    USE SPARINGLY - Returns true if a given item ID is a granted AccountReward item or not an AccountReward item. False if ungranted.
    """


def is_installed_pack(pack: 'int') -> 'bool':
    """
    Return True if the the specified pack is installed and  on this machine. False otherwise.
    """


def remove_sim(sim_id: 'int', zone_id: 'int') -> 'bool':
    """
    Tell C++ that a Sim was destroyed in the zone instance.
    """


def set_initial_unit_rent_prices(zone_id: 'int') -> 'int':
    """
    Sets the initial rent price on the server and client HouseDescriptionResources.
    """


def show_mtx_lock_icon(pack: 'int') -> 'bool':
    """
    Checks if the player should see the mtx lock icon for the given entitlement.
    """
