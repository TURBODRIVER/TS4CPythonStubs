"""
Zone Module.
"""

from typing import *


class Zone():
    """
    Describes the configuration of the active zone.
    """

    def __init__(self, *args):
        pass

    @property
    def active_lot_id(self):
        """
        The active lot id.
        """

    @active_lot_id.setter
    def active_lot_id(self, value):
        """
        The active lot id.
        """

    @property
    def display_name_key(self):
        """
        The displayed name for the zone.
        """

    @display_name_key.setter
    def display_name_key(self, value):
        """
        The displayed name for the zone.
        """

    @property
    def start_pos(self):
        """
        The sim's starting position in the zone.
        """

    @start_pos.setter
    def start_pos(self, value):
        """
        The sim's starting position in the zone.
        """


def add_sim(arg0, arg1):
    """
    Tell C++ that a Sim was created in the zone instance.
    """


def create_venue(arg0, arg1, arg2, arg3, arg4):
    """
    Creates a venue from a household instance id and returns the zone instance id.
    """


def get_building_type(arg0):
    """
    Returns the building type from the house description provided.
    """


def get_eco_footprint_value(arg0):
    """
    Returns the default eco footprint value from the house description provided.
    """


def get_hide_from_lot_picker(kwarg0: Any = None, kwarg1: Any = None):
    """
    Checks if the given lot/world id pair is tuned in catalog side to be hidden from the lot picker UI.
    """


def get_house_description_id(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
    """
    Returns the house description id from the lot template id provided.
    """


def get_is_eco_footprint_compatible_for_world_description():
    """
    Given a world description id, return true if it is eco footprint compatible.
    """


def get_lot_description_id(kwarg0: Any = None, kwarg1: Any = None):
    """
    Returns the lot description id from the lot's id.
    """


def get_rent(arg0):
    """
    Returns the rent amount set on the house description.
    """


def get_signed_lease_length(arg0):
    """
    Returns the lease length amount set on the house description.
    """


def get_world_and_lot_description_id_from_zone_id(arg0):
    """
    Returns the tuple (world description id, lot description id from the zone id.
    """


def get_world_description_id(arg0):
    """
    Returns the world/street description id from the world's id.
    """


def get_world_id(arg0):
    """
    Returns the world id from the world description id.
    """


def has_entitlement(arg0):
    """
    Checks if the given account can use provided entitlement.
    """


def invite_sims_to_zone():
    """
    Requests a travel reservation for remote sims in order to try and pull them to the calling zone.
    """


def is_available_pack(arg0):
    """
    Return True if the the given account is entitled to the specified pack and it is installed on this machine. False otherwise.
    """


def is_displayable(arg0):
    """
    Checks if the entitlement is visible to the player, regardless if the player has the entitlement.
    """


def is_entitled_pack(arg0):
    """
    Return True if the given account is entitled to the specified pack. False otherwise.
    """


def is_event_enabled(arg0):
    """
    Checks if the given event switch is enabled.
    """


def is_granted_or_non_account_reward_item(arg0, arg1):
    """
    USE SPARINGLY - Returns true if a given item ID is a granted AccountReward item or not an AccountReward item. False if ungranted.
    """


def is_installed_pack(arg0):
    """
    Return True if the the specified pack is installed and  on this machine. False otherwise.
    """


def remove_sim(arg0, arg1):
    """
    Tell C++ that a Sim was destroyed in the zone instance.
    """


def set_initial_unit_rent_prices():
    """
    Sets the initial rent price on the server and client HouseDescriptionResources.
    """


def show_mtx_lock_icon(arg0):
    """
    Checks if the player should see the mtx lock icon for the given entitlement.
    """
