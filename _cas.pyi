# Annotations Created by TURBODRIVER

"""
CAS Utilities
"""

from typing import *

import _resourceman
import types

class OutfitData():
    """
    Defines the contents of an outfit, such as ID, parts, etc...
    """

    def __init__(self):
        """
        Defines the contents of an outfit, such as ID, parts, etc...
        """

    @property
    def body_types(self) -> 'Tuple[int, ...]':
        """
        The outfit's body types.
        """

    @body_types.setter
    def body_types(self, value: 'Tuple[int, ...]'):
        """
        The outfit's body types.
        """

    @property
    def cost(self) -> 'int':
        """
        The outfit's cost
        """

    @cost.setter
    def cost(self, value: 'int'):
        """
        The outfit's cost
        """

    def get_parts_ids(self) -> 'Tuple[int, ...]':
        """
        Returns a list of all the Part's IDs
        """

    def has_part_id(self, part_id: 'int') -> 'bool':
        """
        Returns whether or not the outfit has the Part the given key.
        """

    @property
    def match_hair_style(self) -> 'bool':
        """
        Whether or not the outfit matches the default outfit's hair style.
        """

    @match_hair_style.setter
    def match_hair_style(self, value: 'bool'):
        """
        Whether or not the outfit matches the default outfit's hair style.
        """

    @property
    def outfit_category(self) -> 'int':
        """
        The outfit's category.
        """

    @outfit_category.setter
    def outfit_category(self, value: 'int'):
        """
        The outfit's category.
        """

    @property
    def outfit_flags(self) -> 'int':
        """
        The outfit's flags low bits.
        """

    @outfit_flags.setter
    def outfit_flags(self, value: 'int'):
        """
        The outfit's flags low bits.
        """

    @property
    def outfit_flags_full(self) -> 'Tuple[int, int, int]':
        """
        The outfit's flags [low, high1, high2] tuple.
        """

    @outfit_flags_full.setter
    def outfit_flags_full(self, value: 'Tuple[int, int, int]'):
        """
        The outfit's flags [low, high1, high2] tuple.
        """

    @property
    def outfit_flags_high(self) -> 'int':
        """
        The outfit's flags high bits.
        """

    @outfit_flags_high.setter
    def outfit_flags_high(self, value: 'int'):
        """
        The outfit's flags high bits.
        """

    @property
    def outfit_flags_high2(self) -> 'int':
        """
        The outfit's flags additional high bits.
        """

    @outfit_flags_high2.setter
    def outfit_flags_high2(self, value: 'int'):
        """
        The outfit's flags additional high bits.
        """

    @property
    def outfit_id(self) -> 'int':
        """
        The outfit's unique ID.
        """

    @outfit_id.setter
    def outfit_id(self, value: 'int'):
        """
        The outfit's unique ID.
        """

    @property
    def part_hashes(self) -> 'Tuple[int, ...]':
        """
        The outfit's part IDs.
        """

    @part_hashes.setter
    def part_hashes(self, value: 'Tuple[int, ...]'):
        """
        The outfit's part IDs.
        """

    @property
    def part_ids(self) -> 'Tuple[int, ...]':
        """
        The outfit's part IDs.
        """

    @part_ids.setter
    def part_ids(self, value: 'Tuple[int, ...]'):
        """
        The outfit's part IDs.
        """

    @property
    def part_object_ids(self) -> 'Tuple[int, ...]':
        """
        The outfit's part IDs.
        """

    @part_object_ids.setter
    def part_object_ids(self, value: 'Tuple[int, ...]'):
        """
        The outfit's part IDs.
        """

    @property
    def rarity(self) -> 'int':
        """
        The outfit's rarity
        """

    @rarity.setter
    def rarity(self, value: 'int'):
        """
        The outfit's rarity
        """

    @property
    def title(self) -> 'str':
        """
        The outfit's title
        """

    @title.setter
    def title(self, value: 'str'):
        """
        The outfit's title
        """

    @property
    def trend(self) -> 'int':
        """
        The outfit's trend
        """

    @trend.setter
    def trend(self, value: 'int'):
        """
        The outfit's trend
        """


class SimInfo():
    """
    Base class for all primitives.
    """

    def __init__(self, sim_id: 'int' = 0, first_name: 'str' = "", last_name: 'str' = "", breed_name: 'str' = "", full_name_key: 'int' = 0, breed_name_key: 'int' = 0, age: 'int' = 0, gender: 'int' = 0, species: 'int' = 0, skin_tone: 'int' = 1, physique: 'str' = "", skin_tone_val_shift: 'float' = 0.0):
        """
        Base class for all primitives.
        """

    def add_outfit(self, outfit_category: 'int', outfit_data: 'OutfitData') -> 'int':
        """
        Add the specified outfit to the Sim.
        """

    def add_random_variation_to_modifiers(self, variation_scale: 'Optional[float]' = None) -> 'bool':
        """
        Randomly offsets all modifier values.
        """

    @property
    def age(self) -> 'int':
        """
        Get and set the age in SimInfoData.
        """

    @age.setter
    def age(self, value: 'int'):
        """
        Get and set the age in SimInfoData.
        """

    @property
    def aspiration_id(self) -> 'int':
        """
        Get the aspiration id in SimInfoData.
        """

    @aspiration_id.setter
    def aspiration_id(self, value: 'int'):
        """
        Get the aspiration id in SimInfoData.
        """

    @property
    def base_trait_ids(self) -> 'Tuple[int, ...]':
        """
        Get and set trait ids in SimInfoData.
        """

    @base_trait_ids.setter
    def base_trait_ids(self, value: 'Tuple[int, ...]'):
        """
        Get and set trait ids in SimInfoData.
        """

    @property
    def body_frame_gender(self) -> 'int':
        """
        Set the body frame gender in SimInfoData
        """

    @body_frame_gender.setter
    def body_frame_gender(self, value: 'int'):
        """
        Set the body frame gender in SimInfoData
        """

    @property
    def breed_name(self) -> 'str':
        """
        Get and set the breed name in SimInfoData.
        """

    @breed_name.setter
    def breed_name(self, value: 'str'):
        """
        Get and set the breed name in SimInfoData.
        """

    @property
    def breed_name_key(self) -> 'int':
        """
        Get and set the breed name key in SimInfoData.
        """

    @breed_name_key.setter
    def breed_name_key(self, value: 'int'):
        """
        Get and set the breed name key in SimInfoData.
        """

    @property
    def current_occult_types(self) -> 'int':
        """
        Get and set the current occult types in SimInfoData.
        """

    @current_occult_types.setter
    def current_occult_types(self, value: 'int'):
        """
        Get and set the current occult types in SimInfoData.
        """

    @property
    def custom_texture(self) -> 'int':
        """
        Get and set the custom texture id in SimInfoData.
        """

    @custom_texture.setter
    def custom_texture(self, value: 'int'):
        """
        Get and set the custom texture id in SimInfoData.
        """

    @property
    def facial_attributes(self) -> 'str':
        """
        Get and set the facial_attributes in SimInfoData.
        """

    @facial_attributes.setter
    def facial_attributes(self, value: 'str'):
        """
        Get and set the facial_attributes in SimInfoData.
        """

    @property
    def first_name(self) -> 'str':
        """
        Get and set the first name in SimInfoData.
        """

    @first_name.setter
    def first_name(self, value: 'str'):
        """
        Get and set the first name in SimInfoData.
        """

    @property
    def first_name_key(self) -> 'int':
        """
        Get and set the first name key in SimInfoData.
        """

    @first_name_key.setter
    def first_name_key(self, value: 'int'):
        """
        Get and set the first name key in SimInfoData.
        """

    def fixup_ghost_outfits(self) -> 'bool':
        """
        Remove Ghost-specific parts, replace with Genus-appropriate parts. Return TRUE if changes were made.
        """

    @property
    def flags(self) -> 'int':
        """
        Get and set the flags (e.g. hair match) in SimInfoData.
        """

    @flags.setter
    def flags(self, value: 'int'):
        """
        Get and set the flags (e.g. hair match) in SimInfoData.
        """

    @property
    def full_name_key(self) -> 'int':
        """
        Get and set the full name key in SimInfoData.
        """

    @full_name_key.setter
    def full_name_key(self, value: 'int'):
        """
        Get and set the full name key in SimInfoData.
        """

    @property
    def gender(self) -> 'int':
        """
        Get and set the gender in SimInfoData.
        """

    @gender.setter
    def gender(self, value: 'int'):
        """
        Get and set the gender in SimInfoData.
        """

    def generate_club_outfit(self, tag_list: 'Sequence[int]', outfit_category: 'int', outfit_index: 'int', destination_category: 'int', destination_index: 'int', single_or_all_random: 'int') -> 'Tuple[Tuple[int, ...], Tuple[int, ...]]':
        """
        Generate a club outfit and return the list of parts.
        """

    def generate_outfit(self, outfit_category: 'int', outfit_index: 'int' = 0, tag_list: 'Sequence[int]' = (), filter_flag: 'int' = 0, body_type_flags: 'int' = 0, body_type_flags_high: 'int' = 0, exclude_tag_list: 'Sequence[int]' = (), body_type_chance_overrides: 'Optional[Dict[int, float]]' = None, body_type_match_not_found_overrides: 'Optional[Dict[int, int]]' = None, seed: 'Optional[int]' = None) -> 'bool':
        """
        Generate a outfit for the sim's specified outfit category and index using a set of tags. Optional filter flag to affect which parts are considered by the TaggingFilter -- Please see TaggingFilter.h
        """

    @property
    def genetic_data(self) -> 'bytes':
        """
        Get and set the genetic data from/to SimInfoData.
        """

    @genetic_data.setter
    def genetic_data(self, value: 'bytes'):
        """
        Get and set the genetic data from/to SimInfoData.
        """

    def get_current_growth_level(self, body_type: 'int') -> 'Optional[int]':
        """
        Returns the length associated with the current part of the specified body type.
        """

    def get_outfit(self, outfit_category: 'int', outfit_index: 'int') -> 'OutfitData':
        """
        Return the outfit corresponding to the specified category and index.
        """

    def get_outfits_in_category(self, outfit_category: 'int') -> 'Tuple[int, ...]':
        """
        Return all the outfits in the specified category.
        """

    def get_preferred_growth_level(self, body_type: 'int') -> 'Optional[int]':
        """
        Returns the length associated with the preferred part of the specified body type.
        """

    def has_outfit(self, outfit_category: 'int', outfit_index: 'int') -> 'bool':
        """
        Return whether or not an outfit exists for the specified category and index.
        """

    def is_preferred_growth_part(self, body_type: 'int') -> 'bool':
        """
        Returns whether or not the current part is the same as the preferred part for the given body type.
        """

    @property
    def last_name(self) -> 'str':
        """
        Get and set the last in SimInfoData.
        """

    @last_name.setter
    def last_name(self, value: 'str'):
        """
        Get and set the last in SimInfoData.
        """

    @property
    def last_name_key(self) -> 'int':
        """
        Get and set the last name key in SimInfoData.
        """

    @last_name_key.setter
    def last_name_key(self, value: 'int'):
        """
        Get and set the last name key in SimInfoData.
        """

    def load_from_resource(self, resource_key: '_resourceman.Key', age: 'Optional[int]' = None) -> 'bool':
        """
        Requests a load of a SimInfoDataResource with the specified instance id.
        """

    @property
    def occult_types(self) -> 'int':
        """
        Get and set the occult types in SimInfoData.
        """

    @occult_types.setter
    def occult_types(self, value: 'int'):
        """
        Get and set the occult types in SimInfoData.
        """

    @property
    def outfit_type_and_index(self) -> 'Tuple[int, int]':
        """
        Get and set the current outfit type and index in SimInfoData, no update is triggered, not guarded against non-existent outfits.
        """

    @outfit_type_and_index.setter
    def outfit_type_and_index(self, value: 'Tuple[int, int]'):
        """
        Get and set the current outfit type and index in SimInfoData, no update is triggered, not guarded against non-existent outfits.
        """

    @property
    def outfits(self) -> 'bytes':
        """
        Get and set the default outfit in SimInfoData.
        """

    @outfits.setter
    def outfits(self, value: 'bytes'):
        """
        Get and set the default outfit in SimInfoData.
        """

    @property
    def packed_pronouns(self) -> 'str':
        """
        Get and set the packed pronouns in SimInfoData.
        """

    @packed_pronouns.setter
    def packed_pronouns(self, value: 'str'):
        """
        Get and set the packed pronouns in SimInfoData.
        """

    @property
    def parts_custom_tattoos(self) -> 'Dict[int, int]':
        """
        Get and set the Part's custom tattoo texture id in SimInfoData
        """

    @parts_custom_tattoos.setter
    def parts_custom_tattoos(self, value: 'Dict[int, int]'):
        """
        Get and set the Part's custom tattoo texture id in SimInfoData
        """

    @property
    def pelt_layers(self) -> 'str':
        """
        Get and set the pelt layers in SimInfoData.
        """

    @pelt_layers.setter
    def pelt_layers(self, value: 'str'):
        """
        Get and set the pelt layers in SimInfoData.
        """

    @property
    def physique(self) -> 'str':
        """
        Get and set the physique in SimInfoData.
        """

    @physique.setter
    def physique(self, value: 'str'):
        """
        Get and set the physique in SimInfoData.
        """

    @property
    def pronouns(self) -> 'bytes':
        """
        Get and set the pronouns in SimInfoData as SimPronouns.
        """

    @pronouns.setter
    def pronouns(self, value: 'bytes'):
        """
        Get and set the pronouns in SimInfoData as SimPronouns.
        """

    def push_to_relgraph(self) -> 'bool':
        """
        Adds sim to relgraph; updates sim node if sim already in the graph.
        """

    def remove_invalid_face_parts(self) -> 'bool':
        """
        Remove face parts inconsistent with the current genus.
        """

    def remove_outfit(self, outfit_category: 'int', outfit_index: 'int') -> 'bool':
        """
        Remove the outfit corresponding to the specified category and index.
        """

    def remove_unowned_parts(self) -> 'int':
        """
        Removes parts not owned by player from all outfits. Returns number of parts removed.
        """

    @property
    def rig_key(self) -> '_resourceman.Key':
        """
        Get the key for the rig used by this sim.
        """

    @rig_key.setter
    def rig_key(self, value: '_resourceman.Key'):
        """
        Get the key for the rig used by this sim.
        """

    def set_outfit_flags(self, outfit_category: 'int', outfit_index: 'int', outfit_flags_low: 'int', outfit_flags_high: 'int' = 0) -> 'bool':
        """
        Set outfit flags for the specified outfit.
        """

    @property
    def skin_tone(self) -> 'int':
        """
        Get and set the skin tone in SimInfoData.
        """

    @skin_tone.setter
    def skin_tone(self, value: 'int'):
        """
        Get and set the skin tone in SimInfoData.
        """

    @property
    def skin_tone_val_shift(self) -> 'float':
        """
        Get and set the skin tone val shift in SimInfoData.
        """

    @skin_tone_val_shift.setter
    def skin_tone_val_shift(self, value: 'float'):
        """
        Get and set the skin tone val shift in SimInfoData.
        """

    @property
    def species(self) -> 'int':
        """
        Get and set the species in SimInfoData
        """

    @species.setter
    def species(self, value: 'int'):
        """
        Get and set the species in SimInfoData
        """

    @property
    def trait_ids(self) -> 'Tuple[int, ...]':
        """
        Get and set trait ids in SimInfoData.
        """

    @trait_ids.setter
    def trait_ids(self, value: 'Tuple[int, ...]'):
        """
        Get and set trait ids in SimInfoData.
        """

    def update_for_age(self, age: 'int') -> 'bool':
        """
        Ages a sim up to a provided age
        """

    def update_gender_for_traits(self, gender: 'int', trait_ids: 'Sequence[int]') -> 'bool':
        """
        Assigns the given traits to a sim and performs a gender swap if necessary
        """

    @property
    def voice_actor(self) -> 'int':
        """
        Get and set the voice_actor in SimInfoData.
        """

    @voice_actor.setter
    def voice_actor(self, value: 'int'):
        """
        Get and set the voice_actor in SimInfoData.
        """

    @property
    def voice_effect(self) -> 'int':
        """
        Get and set the voice effect in SimInfoData
        """

    @voice_effect.setter
    def voice_effect(self, value: 'int'):
        """
        Get and set the voice effect in SimInfoData
        """

    @property
    def voice_pitch(self) -> 'float':
        """
        Get and set the voice_pitch in SimInfoData.
        """

    @voice_pitch.setter
    def voice_pitch(self, value: 'float'):
        """
        Get and set the voice_pitch in SimInfoData.
        """


def age_up_sim(sim_info: 'SimInfo') -> 'bool':
    """
    Age up the provided sim.
    """


def apply_siminfo_override(original_sim_info: 'SimInfo', modified_sim_info: 'SimInfo', resulting_sim_info: 'SimInfo', option_flags: 'int' = 0, filter_outfit_category_index_pair_dict: 'Optional[Sequence[Tuple[int, int]]]' = None) -> 'bool':
    """
    Applies override to siminfo_in to obtain siminfo_out.
    """


def caspart_has_tag(caspart_id: 'int', tag: 'int') -> 'bool':
    """
    Returns if caspart has any of the defined tags
    """


def change_bodytype_level(sim_info: 'SimInfo', bodytype_level_mapping: 'Dict[int, int]') -> 'SimInfo':
    """
    Return a new siminfo with updated parts based on the given bodytype/level mapping.
    """


def dump_active_modifiers(siminfo_in: 'SimInfo') -> 'List[Tuple[List[Tuple[int, float]], List[Tuple[int, float]]]]':
    """
    Returns caspart body type (e.g. top, bottom, fullbody etc). The only arg is part instance id.
    """


def generate_household(sim_creation_dictionaries: 'Sequence[dict]', household_name: 'str' = "", generate_deterministic_sim: 'bool' = False, generate_all_cas_outfits: 'bool' = False) -> 'Dict[str, Union[int, str, List[bytes]]]':
    """
    Return a dictionary containing household id, household name and list of sims.
    """


def generate_merged_outfit(destination_sim_info: 'SimInfo', source_sim_info: 'SimInfo', destination_category: 'int', destination_index: 'int', template_category: 'int', template_index: 'int', source_category: 'int', source_index: 'int') -> 'bool':
    """
    Generate an outfit for the specified category and index using the two specified category/index pairs and a second SimInfo.
    """


def generate_occult_siminfo(source_sim_info: 'SimInfo', target_sim_info: 'SimInfo', occult_type: 'int') -> 'bool':
    """
    Generates an occult version of the specified SimInfo.
    """


def generate_offspring(parent_a: 'SimInfo', parent_b: 'SimInfo', child_sim_info: 'SimInfo', seed: 'Optional[int]' = None) -> 'bool':
    """
    Return a Sim Info that is an offspring of the two provided Sims.
    """


def generate_random_siminfo(sim_info: 'SimInfo', seed: 'Optional[int]' = None) -> 'bool':
    """
    Generate a randomized SimInfo, preserving the current age/gender/species flags.
    """


def get_buffs_from_part_ids(part_ids: 'Sequence[int]') -> 'Tuple[int, ...]':
    """
    Return a list of buff guids associated with part ids.
    """


def get_caspart_bodytype(caspart_id: 'int') -> 'int':
    """
    Returns caspart body type (e.g. top, bottom, fullbody etc). The only arg is part instance id.
    """


def get_caspart_gender_compatible(sim_info: 'SimInfo', cas_part: 'int') -> 'int':
    """
    Returns the correct part instance id according to sim's info gender frame compatibility.
    """


def get_caspart_hide_occult_flags(caspart_id: 'int') -> 'int':
    """
    Returns caspart occult flags (e.g. vampire, werewolf, etc... etc). The only arg is part instance id.
    """


def get_catalog_casparts_by_bodytype(sim_info: 'SimInfo', include_tags: 'Sequence[int]' = (), exclude_tags: 'Sequence[int]' = (), bodytypes: 'Sequence[int]' = (), show_all_variants: 'bool' = False, rewards_parts: 'Sequence[int]' = ()) -> 'Dict[int, Tuple[Sequence[int], int]]':
    """
    Returns casparts from the catalog with a defined body type.
    """


def get_tags_from_outfit(sim_info: 'SimInfo', outfit_category: 'int', outfit_index: 'int', body_type_filter: 'int' = 0, body_type_flags_filter: 'int' = 0) -> 'Dict[int, Tuple[int, ...]]':
    """
    Returns dictionary with part long instance as keys and set of tags as values. These are tags found for the specified outfit of siminfo.
    """


def is_duplicate_merged_outfit(destination_sim_info: 'SimInfo', source_sim_info: 'SimInfo', template_category: 'int', template_index: 'int', source_category: 'int', source_index: 'int') -> 'bool':
    """
    Checks whether the specified source outfit is a duplicate of the specified template outfit (on self).
    """


def is_online_entitled() -> 'bool':
    """
    Return online entitlement status of the client.
    """


def randomize_caspart(source_sim_info: 'SimInfo', modified_sim_info: 'SimInfo', body_type: 'int', tags_to_keep: 'Sequence[int]' = (), seed: 'int' = 0, tag_list: 'Sequence[int]' = ()) -> 'bool':
    """
    Return siminfo with a randomized caspart for specified bodytype.
    """


def randomize_caspart_list(include_tags: 'Sequence[int]' = (), exclude_tags: 'Sequence[int]' = (), bodytype: 'int' = 0, count: 'int' = 1, seed: 'int' = 0) -> 'List[int]':
    """
    Return list of cas part IDs based on include/exclude tags and body type
    """


def randomize_part_color(source_sim_info: 'SimInfo', modified_sim_info: 'SimInfo', body_type: 'int', seed: 'int' = 0) -> 'bool':
    """
    Returns siminfo with randomly changed color of a caspart of specified bodytype.
    """


def randomize_skintone_from_tags(source_sim_info: 'SimInfo', modified_sim_info: 'SimInfo', tag_list: 'Sequence[int]' = (), seed: 'int' = 0) -> 'bool':
    """
    Returns siminfo with randomly selected skintone.
    """


def relgraph_add_child(parent_a_id: 'int', parent_b_id: 'int', child_sim_id: 'int') -> 'bool':
    """
    Updates relationship graph by adding new sim with none, one or two parents specified. Use SIMID_INVALID in leiu of absent parent.
    """


def relgraph_cull(sim_id_list: 'Sequence[int]', cull_threshold: 'Optional[int]' = None) -> 'bool':
    """
    Culls relationship graph. Takes list of all alive simIds and, optionally, culling depth threshold. Call before saving game or after load completed.
    """


def relgraph_get() -> 'bytes':
    """
    Returns relationship graph (it's CASModule copy) as proto blob.
    """


def relgraph_get_genealogy(sim_id: 'int') -> 'Tuple[int, int, int, int, int, int]':
    """
    From relationship graph, Returns tuple of sim ids (mother, father, mother's mother, mother's father, father's mother, father's father).
    """


def relgraph_set(relgraph_data: 'bytes') -> 'bool':
    """
    Sets relationship graph (it's CASModule copy) from proto blob.
    """


def relgraph_set_edge(sim_id: 'int', target_sim_id: 'int', relationship_type: 'int') -> 'bool':
    """
    Adds (or updates if exists) edge (i.e. relationship) in the relationship graph.
    """


def relgraph_set_engagement(sim_id: 'int', fiance_sim_id: 'int', is_engaged: 'bool') -> 'bool':
    """
    Sets or removes engagement for two sims on relationship graph.
    """


def relgraph_set_marriage(sim_id: 'int', spouse_sim_id: 'int', is_married: 'bool') -> 'bool':
    """
    Sets or removes marriage for two sims on relationship graph.
    """


def relgraph_set_steady(sim_id: 'int', partner_sim_id: 'int', is_steady: 'bool') -> 'bool':
    """
    Sets or removes steady for two sims on relationship graph.
    """


def remove_caspart(source_sim_info: 'SimInfo', modified_sim_info: 'SimInfo', cas_part: 'int', update_genetics: 'bool' = False, object_id: 'int' = 0) -> 'Tuple[int, ...]':
    """
    Returns siminfo with caspart removed.
    """


def remove_caspart_by_bodytype(source_sim_info: 'SimInfo', modified_sim_info: 'SimInfo', body_type: 'int', update_genetics: 'bool' = False, remove_custom_textures: 'bool' = False) -> 'Tuple[int, ...]':
    """
    Returns siminfo with caspart removed.
    """


def revert_modifiers_override(siminfo_in: 'SimInfo', decrement: 'bool' = True, amount: 'float' = 0.0, modifier_id: 'int' = 0) -> 'bool':
    """
    Returns caspart body type (e.g. top, bottom, fullbody etc). The only arg is part instance id.
    """


def set_caspart(source_sim_info: 'SimInfo', modified_sim_info: 'SimInfo', cas_part: 'int', should_toggle: 'bool' = False, replace_with_random: 'bool' = False, update_genetics: 'bool' = False, random_seed: 'int' = 0, remove_conflicting: 'bool' = False, h_shift: 'float' = 0.0, s_shift: 'float' = 0.0, v_shift: 'float' = 0.0, object_id: 'int' = 0, part_layer_index: 'int' = 0, rgba_color_shift: 'int' = 0) -> 'bool':
    """
    Returns siminfo with caspart added. If toggle_part arg is true, and part was already present: it is removed or replaced with random (see args); otherwise: part is added and overrides existing same-type part.
    """
