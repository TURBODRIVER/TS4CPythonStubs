"""
Build Buy Utilities
"""

from typing import *


def add_object_to_buildbuy_system(arg0, arg1):
    """
    Notifies the build/buy system that an object has been created.  (object_id, lot_id) -> bool
    """


def add_object_to_household_inventory(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None, kwarg5: Any = None):
    """
    Moves object to the HouseholdInventory. (objectid, householdid, zoneid, (objectOriginLocation -> uint32 sync with EA::Sims4::BuildBuy::ObjectLocType)
    """


def bb_force_exit(arg0):
    """
    Force a user out of build/buy.  Return true if able to force. (zone_id -> bool)
    """


def begin_update_floor_features(arg0, arg1):
    """
    Begins an update scope for modifying floor feature opacity. (feature_type) -> None
    """


def clear_venue_owner():
    """
    Clear the venue owner, given the active zone id and the current household to clear-> bool
    """


def conditional_layer_destroyed(arg0, arg1):
    """
    Function that is called from Python whenever a conditional layer is destroyed on the script side. (zone_id, layer_hash) -> None
    """


def copy_objectdata_to_household_inventory(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
    """
    Copies objectdata to the HouseholdInventory. (objectdata, householdid, zoneid,
    """


def disown_household_objects():
    """
    Clears the object ownership of all objects on the lot, given a zone id -> bool
    """


def end_update_floor_features(arg0, arg1):
    """
    Ends an update scope for modifying floor feature opacity. (feature_type) -> None
    """


def find_floor_feature(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
    """
    Returns the nearest non-empty location on a level to a point within a radius. (zone_id, feature_type, world_pos, level, [, max_distance]) -> world_pos or None
    """


def find_objects_in_household_inventory(arg0, arg1):
    """
    Returns the object IDs of any object in the Inventory whose definition matches any entry in objectidlist. (objectidlist, householdid, zoneid)
    """


def generate_lot_waypoints(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None, kwarg5: Any = None, kwarg6: Any = None, kwarg7: Any = None):
    """
    Return generated waypoints for the specified zone (zone_id, plex_id, num_waypoints, sim_location, routing_surface, outside_only, min_depth, max_depth, routing_client, ignore_objects) -> dict key=blockId value=[[Vector3]] | None
    """


def get_active_lot_decoration(arg0, arg1, arg2, arg3):
    """
    Sets (or clears) trim decoration state on the active lot, for holiday customization.  (zone_id, holiday_id, trim_type, trim_instance_id, isClear, level) -> bool
    """


def get_all_block_polygons(arg0, arg1):
    """
    Return block polygon information for the specified zone -> dict key=block_id, value=compound polygon, level
    """


def get_block_id(arg0, arg1, arg2):
    """
    Returns block id for the given world position (zone_id, world_position, lot_level) -> uint
    """


def get_current_venue(kwarg0: Any = None, kwarg1: Any = None):
    """
    Returns venue type of the active lot.  By default, if the venue is not qualified, generic type is returned (zoneid -> uint64).  Optional bool to allow incomplete venue types to be returned.
    """


def get_current_venue_config(arg0):
    """
    Returns the configuration bytes (raw) for the current venue.  For most venue types, this is None (zoneid -> uint64)
    """


def get_current_venue_owner_id():
    """
    Returns the venue owner id for the active lot.
    """


def get_floor_feature(arg0, arg1, arg2, arg3):
    """
    Gets the opacity of a floor feature layer on a tile. (zone_id, feature_type, world_pos, level) -> float
    """


def get_furnished_lot_value():
    """
    Returns furnished lot value (zone_id, isFurnished) -> int
    """


def get_gig_end_tiles(arg0):
    """
    Returns the final number of tiles on the lot at the end of the gig (zone_id) -> int
    """


def get_gig_objects_added(arg0):
    """
    Returns a list of all object instance ids that were added during the gig (zone_id) -> [object ids ]
    """


def get_gig_objects_deleted(arg0):
    """
    Returns a list of all object instance ids that were deleted during the gig (zone_id) -> [object ids]
    """


def get_gig_start_tiles(arg0):
    """
    Returns the number of tiles on the lot at the start of the gig (zone_id) -> int
    """


def get_gig_tag_changes(arg0):
    """
    Returns a list of all tags with the count of instances that changed during the gig (zone_id) -> [ (tag ids, count)]
    """


def get_gig_tags_added(arg0):
    """
    Returns a list of all tags that belong to walls, objects, etc, that were added during the gig (zone_id) -> [ tag ids]
    """


def get_gig_tags_removed(arg0):
    """
    Returns a list of all tags that belong to walls, objects, etc, that were deleted during the gig (zone_id) -> [ tag ids]
    """


def get_gig_tiles_changed(arg0):
    """
    Returns the number of tiles changed during the gig (zone_id) -> int
    """


def get_highest_level_allowed(*args):
    """
    Returns the highest valid level that a lot can have.
    """


def get_household_inventory_value(arg0):
    """
    Returns the value of all objects in the household inventory (householdid)
    """


def get_location_plex_id(arg0, arg1, arg2):
    """
    Returns the plex ID for a given world position (zone_id, world_position, lot_level) -> uint32
    """


def get_lowest_level_allowed(*args):
    """
    Returns the lowest valid level that a lot can have.
    """


def get_object_all_tags(arg0):
    """
    Returns tuple of tags associated with an object (objdefguid) -> uint16 tuple
    """


def get_object_and_style_all_tags(arg0):
    """
    Returns tuple of tags associated with an object and for any styles on the object (objdefguid) -> uint16 tuple
    """


def get_object_buy_category_flags(arg0):
    """
    Return the BuyCategory flags for the given object type. (objdefguid -> uint32)
    """


def get_object_can_depreciate(arg0):
    """
    Return whether the object can depreciate. (objdefguid -> bool)
    """


def get_object_catalog_description(arg0):
    """
    Return the catalog description for the given object type. (objdefguid -> uint32)
    """


def get_object_catalog_name(arg0):
    """
    Return the catalog name for the given object type. (objdefguid -> uint32)
    """


def get_object_data_in_household_inventory(arg0, arg1):
    """
    Returns the object data for the specified object in the Inventory.
    """


def get_object_decosize(arg0):
    """
    Returns the deco slot size associated with a given object type (objdefguid) -> int
    """


def get_object_has_tag(arg0, arg1):
    """
    Returns whether or not an object type has a given tag (objdefguid, tag) -> bool
    """


def get_object_ids_in_household_inventory(arg0):
    """
    Returns object ID of any object in the Inventory.
    """


def get_object_is_deletable(arg0):
    """
    Return whether the object is deletable. (objdefguid -> bool)
    """


def get_object_or_style_has_tag(arg0, arg1):
    """
    Returns whether or not an object type or any styles for the type has a given tag (objdefguid, tag) -> bool
    """


def get_object_pack_by_key(arg0, arg1, arg2):
    """
    Return the Pack Id of the provided object resource key. get_object_pack_by_key(type_id, instance_id, group_id)
    """


def get_object_placement_flags(arg0):
    """
    Return the Placement flags for the given object type. (objdefguid -> uint32)
    """


def get_object_slotset(arg0):
    """
    Returns the resource key for the slot set tuning data associated with a given object type (objdefguid) -> resource key
    """


def get_plex_outline(arg0, arg1, arg2):
    """
    Returns the outline of a plex on a given level (zone_id, lot_level) -> list of blocks, each block is a list of polygons where the first is the outermost, each polygon is a list of points assumed to be a loop
    """


def get_plex_tile_count(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
    """
    Returns the tile count of a plex on a given zone (plex_id, zone_id) -> int
    """


def get_pond_contours_for_wading_depth(arg0, arg1, arg2, arg3):
    """
    Returns the pond geometry for a given depth
    """


def get_pond_edges(arg0):
    """
    Returns pond edges for the lot (zone_id) -> dict key=(pond_id) value=list of (start pt, end pt)
    """


def get_pond_id(arg0, arg1):
    """
    Returns pond id for the given world position (zone_id, world_position) -> uint
    """


def get_pool_edges(arg0):
    """
    Returns pool edges for the lot (zone_id) -> dict key=(block_id, level) value=list of (start pt, end pt)
    """


def get_pool_polys(arg0, arg1, arg2):
    """
    Returns a vector of vectors of points represent. The first vector represents the body of the pool and subsequent vectors represent the holes of the pool. (pool_block_id, zone_id, level) -> [[Vector3]] | None
    """


def get_pool_size_at_location(arg0, arg1, arg2):
    """
    Returns the size of the pool unless the location is not a pool, in which case it returns None. (zone_id, world_position, lot_level) -> uint|None
    """


def get_portal_height_offset_threshold(*args):
    """
    Get the Portal Height offset threshold between the floor surfaces on either side of a wall.
    """


def get_replacement_object(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None, kwarg5: Any = None):
    """
    Returns a new object to replace the current one that can fit in the same spot. pass 0 to num_tries to have it be not limited, error_margin is in centimiters, tags can filter objects to only those that have a one of the tags, exclude objects with any tags; the use of tags allows no catalog items (objectid, num_tries, error_margin, tags, exclude_tags) -> objdefguid
    """


def get_room_id(arg0, arg1, arg2):
    """
    Returns room id for the given world position (zone_id, world_position, lot_level) -> uint
    """


def get_stair_count(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None):
    """
    Retrieve the stair count for an object (object_id, lot_id) -> uint32
    """


def get_user_in_bb(arg0):
    """
    Returns id of user in Build/Buy in a given zone. (zone_id -> int)
    """


def get_variant_group_id(arg0):
    """
    Returns the variant group id for the given object definition id. (objdefguid) -> uint64
    """


def get_venue_tier(arg0):
    """
    Returns venue tier of the lot. (zoneId -> int32)
    """


def get_vetted_object_defn_guid(arg0, arg1, arg2):
    """
    Return a validated object defn guid for the one provided; None if nothing is valid; different if fallback needed; same if already valid (zoneId, objID, objdefguid) -> objdefguid
    """


def get_wall_contours(arg0, arg1, arg2, arg3):
    """
    Return the current wall geometry.  Function takes three arguments; the source x and z positions, and whether to return all the contours, or only the contours facing the source.
    """


def has_any_objects_in_household_inventory(arg0, arg1, arg2, arg3):
    """
    Returns if any of the passed objects exist in the the Inventory. (objectidlist, householdid, zoneid)
    """


def has_floor_at_location(arg0, arg1, arg2):
    """
    Returns true or false if the given world position contains a floor tile at the given lot level(zone_id, world_position, lot_level) -> bool
    """


def has_floor_feature(arg0, arg1, arg2, arg3):
    """
    Checks if a floor feature is present on a tile. (zone_id, feature_type, world_pos, level) -> bool
    """


def init_bb_force_exit(arg0):
    """
    Initiates kicking current user out of Build/Buy in a given zone.  Returns true if user is in BB.  (zone_id -> bool)
    """


def invalidate_object_location(arg0, arg1):
    """
    Notifies the build/buy system that an object has been relocated.  (object_id, lot_id) -> bool
    """


def is_household_inventory_available(arg0):
    """
    Returns true if household inventory is available to add objects to. (household_id)
    """


def is_location_natural_ground(arg0, arg1, arg2):
    """
    Returns true or false if the given world position contains a floor tile marked as natural ground at the given lot level(zone_id, world_position, lot_level) -> bool
    """


def is_location_outside(arg0, arg1, arg2):
    """
    Returns true or false if the given world position is not under a roof or floor tile at the given lot level(zone_id, world_position, lot_level) -> bool
    """


def is_location_pool(arg0, arg1, arg2):
    """
    Returns true or false if the given world position contains a pool lot level(zone_id, world_position, lot_level) -> bool
    """


def list_floor_features(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
    """
    Returns the location of all non-empty locations on a floor feature layer. (zone_id, feature_type [, level]) -> [(world_pos, level)...]
    """


def load_conditional_objects(arg0, arg1, arg2):
    """
    Load a specified number of objects from the conditional layer of the provided layer hash and return a tuple with the first item set to true if all the objects in the layer have been loaded and the second item is a list of the created object ids. Using -1 will load all the objects of a layer.(zone_id, layer_hash, num_objects) -> (all_objects_loaded, [ids])
    """


def mark_conditional_objects_loaded(arg0, arg1, arg2):
    """
    Mark a list of objects of a conditional layer as loaded. (zone_id, layer_hash, objectidlist) -> None
    """


def object_exists_in_household_inventory(arg0, arg1):
    """
    Returns true if the bassinet with the sim id exists in the the Inventory. (objectid, householdid, zoneid)
    """


def register_on_build_buy_wall_update_callback(*args):
    """
    Register a function that is called whenever the wall structure has changed
    """


def remove_object_from_buildbuy_system(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
    """
    Notifies the build/buy system that an object has been destroyed.  (object_id, lot_id) -> bool
    """


def remove_object_from_household_inventory(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
    """
    Removes the object from the HouseholdInventory (objectid, householdid, zoneid, (updateFunds -> bool))
    """


def request_season_weather_interpolation(arg0, arg1, arg2, arg3, arg4, arg5):
    """
    Notifies the simulator when a seasonal interpolation is requested. (zone_id, season_weather_param, start_time, end_time, start_value, end_value) -> None
    """


def reset_conditional_objects(arg0, arg1):
    """
    Reset the stored index representing the next object to create for a conditional layer of the provided layer hash. (zone_id, layer_hash) -> None
    """


def scan_floor_features(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
    """
    Returns a summary of all non-empty locations on a floor feature layer. (zone_id, feature_type [, level]) -> (area, sum)
    """


def set_active_lot_decoration(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None, kwarg5: Any = None, kwarg6: Any = None):
    """
    Gets trim decoration state on the active lot, for holiday customization.  (zone_id, holiday_id, trim_type, level) -> trim_instance_id
    """


def set_client_conditional_layer_active(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None, kwarg5: Any = None, kwarg6: Any = None):
    """
    Load/unload a conditional layer as client-only objects (zone id, account id, layer hash, is load) -> None
    """


def set_floor_feature(arg0, arg1, arg2, arg3, arg4):
    """
    Sets the opacity of a floor feature layer on a tile. This must be done within begin/end update. (zone_id, feature_type, world_pos, level, opacity) -> None
    """


def set_plex_visibility(arg0, arg1, arg2):
    """
    Updates the visibility status of visibility-togglable plexes. Only supported on plex-containing lots where plexes do not define zone partitions.
    """


def set_venue_owner_id():
    """
    Clear venue owner id of lot.
    """


def test_location_for_object(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None, kwarg5: Any = None):
    """
    Returns whether or not an object with the given definition could be placed at the given location. All arguments are optional, but either obj or both location and definition_id must be specified.  Specifying either location or definition_id will override the current values for obj. (obj, definition_id, location, objects_to_ignore, definition_obj_state_index) -> (bool, errors)
    """


def update_gameplay_unlocked_products():
    """
    Updates the list of currently gameplay unlocked objects. (objectlist, zoneid, accountid
    """


def update_object_attributes(arg0, arg1, arg2):
    """
    Updates an attributes field for an object (object_id, serialized_protobuf) -> bool
    """
