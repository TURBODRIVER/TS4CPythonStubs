"""
CAS Utilities
"""

from typing import *


class OutfitData():
    """
    Defines the contents of an outfit, such as ID, parts, etc...
    """

    def __init__(self, *args):
        pass

    @property
    def body_types(self):
        """
        The outfit's body types.
        """

    @body_types.setter
    def body_types(self, value):
        """
        The outfit's body types.
        """

    @property
    def cost(self):
        """
        The outfit's cost
        """

    @cost.setter
    def cost(self, value):
        """
        The outfit's cost
        """

    def get_parts_ids(self):
        """
        Returns a list of all the Part's IDs
        """

    def has_part_id(self):
        """
        Returns whether or not the outfit has the Part the given key.
        """

    @property
    def match_hair_style(self):
        """
        Whether or not the outfit matches the default outfit's hair style.
        """

    @match_hair_style.setter
    def match_hair_style(self, value):
        """
        Whether or not the outfit matches the default outfit's hair style.
        """

    @property
    def outfit_category(self):
        """
        The outfit's category.
        """

    @outfit_category.setter
    def outfit_category(self, value):
        """
        The outfit's category.
        """

    @property
    def outfit_flags(self):
        """
        The outfit's flags low bits.
        """

    @outfit_flags.setter
    def outfit_flags(self, value):
        """
        The outfit's flags low bits.
        """

    @property
    def outfit_flags_full(self):
        """
        The outfit's flags [low, high1, high2] tuple.
        """

    @outfit_flags_full.setter
    def outfit_flags_full(self, value):
        """
        The outfit's flags [low, high1, high2] tuple.
        """

    @property
    def outfit_flags_high(self):
        """
        The outfit's flags high bits.
        """

    @outfit_flags_high.setter
    def outfit_flags_high(self, value):
        """
        The outfit's flags high bits.
        """

    @property
    def outfit_flags_high2(self):
        """
        The outfit's flags additional high bits.
        """

    @outfit_flags_high2.setter
    def outfit_flags_high2(self, value):
        """
        The outfit's flags additional high bits.
        """

    @property
    def outfit_id(self):
        """
        The outfit's unique ID.
        """

    @outfit_id.setter
    def outfit_id(self, value):
        """
        The outfit's unique ID.
        """

    @property
    def part_hashes(self):
        """
        The outfit's part IDs.
        """

    @part_hashes.setter
    def part_hashes(self, value):
        """
        The outfit's part IDs.
        """

    @property
    def part_ids(self):
        """
        The outfit's part IDs.
        """

    @part_ids.setter
    def part_ids(self, value):
        """
        The outfit's part IDs.
        """

    @property
    def part_object_ids(self):
        """
        The outfit's part IDs.
        """

    @part_object_ids.setter
    def part_object_ids(self, value):
        """
        The outfit's part IDs.
        """

    @property
    def rarity(self):
        """
        The outfit's rarity
        """

    @rarity.setter
    def rarity(self, value):
        """
        The outfit's rarity
        """

    @property
    def title(self):
        """
        The outfit's title
        """

    @title.setter
    def title(self, value):
        """
        The outfit's title
        """

    @property
    def trend(self):
        """
        The outfit's trend
        """

    @trend.setter
    def trend(self, value):
        """
        The outfit's trend
        """


class SimInfo():
    """
    Base class for all primitives.
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None, kwarg5: Any = None, kwarg6: Any = None, kwarg7: Any = None, kwarg8: Any = None, kwarg9: Any = None, kwarg10: Any = None, kwarg11: Any = None):
        pass

    def add_outfit(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        Add the specified outfit to the Sim.
        """

    def add_random_variation_to_modifiers(self):
        """
        Randomly offsets all modifier values.
        """

    @property
    def age(self):
        """
        Get and set the age in SimInfoData.
        """

    @age.setter
    def age(self, value):
        """
        Get and set the age in SimInfoData.
        """

    @property
    def aspiration_id(self):
        """
        Get the aspiration id in SimInfoData.
        """

    @aspiration_id.setter
    def aspiration_id(self, value):
        """
        Get the aspiration id in SimInfoData.
        """

    @property
    def base_trait_ids(self):
        """
        Get and set trait ids in SimInfoData.
        """

    @base_trait_ids.setter
    def base_trait_ids(self, value):
        """
        Get and set trait ids in SimInfoData.
        """

    @property
    def body_frame_gender(self):
        """
        Set the body frame gender in SimInfoData
        """

    @body_frame_gender.setter
    def body_frame_gender(self, value):
        """
        Set the body frame gender in SimInfoData
        """

    @property
    def breed_name(self):
        """
        Get and set the breed name in SimInfoData.
        """

    @breed_name.setter
    def breed_name(self, value):
        """
        Get and set the breed name in SimInfoData.
        """

    @property
    def breed_name_key(self):
        """
        Get and set the breed name key in SimInfoData.
        """

    @breed_name_key.setter
    def breed_name_key(self, value):
        """
        Get and set the breed name key in SimInfoData.
        """

    @property
    def current_occult_types(self):
        """
        Get and set the current occult types in SimInfoData.
        """

    @current_occult_types.setter
    def current_occult_types(self, value):
        """
        Get and set the current occult types in SimInfoData.
        """

    @property
    def custom_texture(self):
        """
        Get and set the custom texture id in SimInfoData.
        """

    @custom_texture.setter
    def custom_texture(self, value):
        """
        Get and set the custom texture id in SimInfoData.
        """

    @property
    def facial_attributes(self):
        """
        Get and set the facial_attributes in SimInfoData.
        """

    @facial_attributes.setter
    def facial_attributes(self, value):
        """
        Get and set the facial_attributes in SimInfoData.
        """

    @property
    def first_name(self):
        """
        Get and set the first name in SimInfoData.
        """

    @first_name.setter
    def first_name(self, value):
        """
        Get and set the first name in SimInfoData.
        """

    @property
    def first_name_key(self):
        """
        Get and set the first name key in SimInfoData.
        """

    @first_name_key.setter
    def first_name_key(self, value):
        """
        Get and set the first name key in SimInfoData.
        """

    def fixup_ghost_outfits(self):
        """
        Remove Ghost-specific parts, replace with Genus-appropriate parts. Return TRUE if changes were made.
        """

    @property
    def flags(self):
        """
        Get and set the flags (e.g. hair match) in SimInfoData.
        """

    @flags.setter
    def flags(self, value):
        """
        Get and set the flags (e.g. hair match) in SimInfoData.
        """

    @property
    def full_name_key(self):
        """
        Get and set the full name key in SimInfoData.
        """

    @full_name_key.setter
    def full_name_key(self, value):
        """
        Get and set the full name key in SimInfoData.
        """

    @property
    def gender(self):
        """
        Get and set the gender in SimInfoData.
        """

    @gender.setter
    def gender(self, value):
        """
        Get and set the gender in SimInfoData.
        """

    def generate_club_outfit(self, arg0, arg1, arg2, arg3, arg4, arg5):
        """
        Generate a club outfit and return the list of parts.
        """

    def generate_outfit(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None, kwarg5: Any = None, kwarg6: Any = None, kwarg7: Any = None, kwarg8: Any = None, kwarg9: Any = None, kwarg10: Any = None):
        """
        Generate a outfit for the sim's specified outfit category and index using a set of tags. Optional filter flag to affect which parts are considered by the TaggingFilter -- Please see TaggingFilter.h
        """

    @property
    def genetic_data(self):
        """
        Get and set the genetic data from/to SimInfoData.
        """

    @genetic_data.setter
    def genetic_data(self, value):
        """
        Get and set the genetic data from/to SimInfoData.
        """

    def get_current_growth_level(self):
        """
        Returns the length associated with the current part of the specified body type.
        """

    def get_outfit(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        Return the outfit corresponding to the specified category and index.
        """

    def get_outfits_in_category(self, kwarg0: Any = None):
        """
        Return all the outfits in the specified category.
        """

    def get_preferred_growth_level(self):
        """
        Returns the length associated with the preferred part of the specified body type.
        """

    def has_outfit(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        Return whether or not an outfit exists for the specified category and index.
        """

    def is_preferred_growth_part(self):
        """
        Returns whether or not the current part is the same as the preferred part for the given body type.
        """

    @property
    def last_name(self):
        """
        Get and set the last in SimInfoData.
        """

    @last_name.setter
    def last_name(self, value):
        """
        Get and set the last in SimInfoData.
        """

    @property
    def last_name_key(self):
        """
        Get and set the last name key in SimInfoData.
        """

    @last_name_key.setter
    def last_name_key(self, value):
        """
        Get and set the last name key in SimInfoData.
        """

    def load_from_resource(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
        """
        Requests a load of a SimInfoDataResource with the specified instance id.
        """

    @property
    def occult_types(self):
        """
        Get and set the occult types in SimInfoData.
        """

    @occult_types.setter
    def occult_types(self, value):
        """
        Get and set the occult types in SimInfoData.
        """

    @property
    def outfit_type_and_index(self):
        """
        Get and set the current outfit type and index in SimInfoData, no update is triggered, not guarded against non-existent outfits.
        """

    @outfit_type_and_index.setter
    def outfit_type_and_index(self, value):
        """
        Get and set the current outfit type and index in SimInfoData, no update is triggered, not guarded against non-existent outfits.
        """

    @property
    def outfits(self):
        """
        Get and set the default outfit in SimInfoData.
        """

    @outfits.setter
    def outfits(self, value):
        """
        Get and set the default outfit in SimInfoData.
        """

    @property
    def packed_pronouns(self):
        """
        Get and set the packed pronouns in SimInfoData.
        """

    @packed_pronouns.setter
    def packed_pronouns(self, value):
        """
        Get and set the packed pronouns in SimInfoData.
        """

    @property
    def parts_custom_tattoos(self):
        """
        Get and set the Part's custom tattoo texture id in SimInfoData
        """

    @parts_custom_tattoos.setter
    def parts_custom_tattoos(self, value):
        """
        Get and set the Part's custom tattoo texture id in SimInfoData
        """

    @property
    def pelt_layers(self):
        """
        Get and set the pelt layers in SimInfoData.
        """

    @pelt_layers.setter
    def pelt_layers(self, value):
        """
        Get and set the pelt layers in SimInfoData.
        """

    @property
    def physique(self):
        """
        Get and set the physique in SimInfoData.
        """

    @physique.setter
    def physique(self, value):
        """
        Get and set the physique in SimInfoData.
        """

    @property
    def pronouns(self):
        """
        Get and set the pronouns in SimInfoData as SimPronouns.
        """

    @pronouns.setter
    def pronouns(self, value):
        """
        Get and set the pronouns in SimInfoData as SimPronouns.
        """

    def push_to_relgraph(self):
        """
        Adds sim to relgraph; updates sim node if sim already in the graph.
        """

    def remove_invalid_face_parts(self):
        """
        Remove face parts inconsistent with the current genus.
        """

    def remove_outfit(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        Remove the outfit corresponding to the specified category and index.
        """

    def remove_unowned_parts(self):
        """
        Removes parts not owned by player from all outfits. Returns number of parts removed.
        """

    @property
    def rig_key(self):
        """
        Get the key for the rig used by this sim.
        """

    @rig_key.setter
    def rig_key(self, value):
        """
        Get the key for the rig used by this sim.
        """

    def set_outfit_flags(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
        """
        Set outfit flags for the specified outfit.
        """

    @property
    def skin_tone(self):
        """
        Get and set the skin tone in SimInfoData.
        """

    @skin_tone.setter
    def skin_tone(self, value):
        """
        Get and set the skin tone in SimInfoData.
        """

    @property
    def skin_tone_val_shift(self):
        """
        Get and set the skin tone val shift in SimInfoData.
        """

    @skin_tone_val_shift.setter
    def skin_tone_val_shift(self, value):
        """
        Get and set the skin tone val shift in SimInfoData.
        """

    @property
    def species(self):
        """
        Get and set the species in SimInfoData
        """

    @species.setter
    def species(self, value):
        """
        Get and set the species in SimInfoData
        """

    @property
    def trait_ids(self):
        """
        Get and set trait ids in SimInfoData.
        """

    @trait_ids.setter
    def trait_ids(self, value):
        """
        Get and set trait ids in SimInfoData.
        """

    def update_for_age(self):
        """
        Ages a sim up to a provided age
        """

    def update_gender_for_traits(self):
        """
        Assigns the given traits to a sim and performs a gender swap if necessary
        """

    @property
    def voice_actor(self):
        """
        Get and set the voice_actor in SimInfoData.
        """

    @voice_actor.setter
    def voice_actor(self, value):
        """
        Get and set the voice_actor in SimInfoData.
        """

    @property
    def voice_effect(self):
        """
        Get and set the voice effect in SimInfoData
        """

    @voice_effect.setter
    def voice_effect(self, value):
        """
        Get and set the voice effect in SimInfoData
        """

    @property
    def voice_pitch(self):
        """
        Get and set the voice_pitch in SimInfoData.
        """

    @voice_pitch.setter
    def voice_pitch(self, value):
        """
        Get and set the voice_pitch in SimInfoData.
        """


def age_up_sim(arg0):
    """
    Age up the provided sim.
    """


def apply_siminfo_override(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
    """
    Applies override to siminfo_in to obtain siminfo_out.
    """


def caspart_has_tag():
    """
    Returns if caspart has any of the defined tags
    """


def change_bodytype_level():
    """
    Return a new siminfo with updated parts based on the given bodytype/level mapping.
    """


def dump_active_modifiers(kwarg0: Any = None):
    """
    Returns caspart body type (e.g. top, bottom, fullbody etc). The only arg is part instance id.
    """


def generate_household(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None):
    """
    Return a dictionary containing household id, household name and list of sims.
    """


def generate_merged_outfit(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
    """
    Generate an outfit for the specified category and index using the two specified category/index pairs and a second SimInfo.
    """


def generate_occult_siminfo(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
    """
    Generates an occult version of the specified SimInfo.
    """


def generate_offspring(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None):
    """
    Return a Sim Info that is an offspring of the two provided Sims.
    """


def generate_random_siminfo(kwarg0: Any = None, kwarg1: Any = None):
    """
    Generate a randomized SimInfo, preserving the current age/gender/species flags.
    """


def get_buffs_from_part_ids(arg0):
    """
    Return a list of buff guids associated with part ids.
    """


def get_caspart_bodytype():
    """
    Returns caspart body type (e.g. top, bottom, fullbody etc). The only arg is part instance id.
    """


def get_caspart_gender_compatible(kwarg0: Any = None, kwarg1: Any = None):
    """
    Returns the correct part instance id according to sim's info gender frame compatibility.
    """


def get_caspart_hide_occult_flags():
    """
    Returns caspart occult flags (e.g. vampire, werewolf, etc... etc). The only arg is part instance id.
    """


def get_catalog_casparts_by_bodytype(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None, kwarg5: Any = None):
    """
    Returns casparts from the catalog with a defined body type.
    """


def get_tags_from_outfit():
    """
    Returns dictionary with part long instance as keys and set of tags as values. These are tags found for the specified outfit of siminfo.
    """


def is_duplicate_merged_outfit(arg0, arg1, arg2, arg3, arg4, arg5):
    """
    Checks whether the specified source outfit is a duplicate of the specified template outfit (on self).
    """


def is_online_entitled(*args):
    """
    Return online entitlement status of the client.
    """


def randomize_caspart(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None, kwarg5: Any = None):
    """
    Return siminfo with a randomized caspart for specified bodytype.
    """


def randomize_caspart_list(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
    """
    Return list of cas part IDs based on include/exclude tags and body type
    """


def randomize_part_color(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None):
    """
    Returns siminfo with randomly changed color of a caspart of specified bodytype.
    """


def randomize_skintone_from_tags(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None):
    """
    Returns siminfo with randomly selected skintone.
    """


def relgraph_add_child(arg0, arg1, arg2):
    """
    Updates relationship graph by adding new sim with none, one or two parents specified. Use SIMID_INVALID in leiu of absent parent.
    """


def relgraph_cull(kwarg0: Any = None, kwarg1: Any = None):
    """
    Culls relationship graph. Takes list of all alive simIds and, optionally, culling depth threshold. Call before saving game or after load completed.
    """


def relgraph_get(*args):
    """
    Returns relationship graph (it's CASModule copy) as proto blob.
    """


def relgraph_get_genealogy(arg0):
    """
    From relationship graph, Returns tuple of sim ids (mother, father, mother's mother, mother's father, father's mother, father's father).
    """


def relgraph_set():
    """
    Sets relationship graph (it's CASModule copy) from proto blob.
    """


def relgraph_set_edge(arg0, arg1, arg2):
    """
    Adds (or updates if exists) edge (i.e. relationship) in the relationship graph.
    """


def relgraph_set_engagement(arg0, arg1, arg2):
    """
    Sets or removes engagement for two sims on relationship graph.
    """


def relgraph_set_marriage(arg0, arg1, arg2):
    """
    Sets or removes marriage for two sims on relationship graph.
    """


def relgraph_set_steady(arg0, arg1, arg2):
    """
    Sets or removes steady for two sims on relationship graph.
    """


def remove_caspart():
    """
    Returns siminfo with caspart removed.
    """


def remove_caspart_by_bodytype():
    """
    Returns siminfo with caspart removed.
    """


def revert_modifiers_override(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None):
    """
    Returns caspart body type (e.g. top, bottom, fullbody etc). The only arg is part instance id.
    """


def set_caspart():
    """
    Returns siminfo with caspart added. If toggle_part arg is true, and part was already present: it is removed or replaced with random (see args); otherwise: part is added and overrides existing same-type part.
    """
