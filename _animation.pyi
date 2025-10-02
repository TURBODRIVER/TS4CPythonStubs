"""
Native services for sims4 animation runtime
"""

from typing import *


class ArbBase():
    """
    ArbBase provides the native-side functionality for the animation.arb.Arb type.
    """

    def __init__(self, *args):
        _native_handle: Any  # Native ARB handle owned by this instance

    def _actor_instances(self):
        """
        Returns a tuple of (actor_id, suffix tuples listing actor instances affected by this arb
        """

    def _actors(self) -> "list":
        """
        Returns a tuple of actor ids affected by this arb
        """

    def _add_custom_event(self, actor_id, base_time, time_in_secs, event_id, allow_create_stub=False) -> "bool":
        """
        adds a procedural event with id event_id to the arb for the given actor
        at the time in seconds from the base time (start or end of controller
        """

    def _append(self, arb, safe_mode=True, force_sync=False) -> "bool":
        pass

    def _begin_synchronized_group(self):
        """
        Begins a synchronized scheduling group
        """

    def _bytes(self):
        """
        Returns the contents of the ARB as bytes
        """

    def _can_append(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        _append(arbToAppend, safeMode=True)
        """

    def _end_synchronized_group(self):
        """
        Ends a synchronized scheduling group
        """

    def _ends_in_looping_content(self, actor_id, min_track_id) -> "bool":
        """
        Returns True if the last content for the specified actor/track pair
        is looping (infinite duration; False otherwise
        """

    def _events(self) -> "list":
        """
        Returns a tuple of events from this arb
        """

    def _get_boundary_conditions(self, actor_id):
        """
        Returns the pre/post-conditions (for positioning for the the specified actor based on the
        contents of the ARB.  The pre-condition is specified as an offset from the scene origin,which is assumed to be the transform of the 'target object'.  The post-condition is explicitlyreturned as an offset plus an object ID from which the offset is relative.
        """

    def _get_timing(self) -> "Tuple[float, float, float]":
        """
        get_timing() - Returns a tuple of (maximum_duration, minimum_duration) for the ARB contents
        """

    def _is_interruptible(self):
        """
        _bytes() - Returns true if the arb is interruptible
        """

    def _normal_timeline_ends_in_looping_content(self, actor_id):
        """
        Returns True if the last content for the specified actor on the normal timeline
        is looping (infinite duration; False otherwise
        """

    def _should_analyze(self):
        """
        _bytes() - Returns true if the arb is needs to be analyzed ahead of time on the client (usually this is set if it contains an authored path)
        """

    @property
    def empty(self):
        """
        _empty() - Returns True if the ARB contains no controllers
        """

    @empty.setter
    def empty(self, value):
        """
        _empty() - Returns True if the ARB contains no controllers
        """

    def get_contents_as_string(self):
        """
        Returns the contents of this arb as a formatted text string
        """

    def get_estimated_duration(self) -> "float":
        """
        Returns the estimated duration (in seconds of the ARB contents
        """

    def is_valid(self) -> "bool":
        """
        Returns 'True' if all ARB contents are valid, 'False' otherwise.
        """

    @property
    def master_actor_id(self):
        """
        Return a reasonable master actor id, for e.g. distribution purposes
        """

    @master_actor_id.setter
    def master_actor_id(self, value):
        """
        Return a reasonable master actor id, for e.g. distribution purposes
        """

    @property
    def network_id(self):
        """
        _empty() - Returns True if the ARB contains no controllers
        """

    @network_id.setter
    def network_id(self, value):
        """
        _empty() - Returns True if the ARB contains no controllers
        """

    def preload(self, *args):
        """
        Issue preload requests for all essential content
        """

    def schedule(self, actor_id, controller, priority=10000, blend_in=-1.0, blend_out=-1.0):
        """
        Schedules a controller on the given actor, created from the CSL-formatted
        string provided in 'controller'.
        """


class AsmBase():
    """
    AsmBase provides the native-side functionality for the animation.Asm type.
    """

    def __init__(self, key):
        _native_handle: Any  # Native ASM handle owned by this instance

    def _add_actor_instance_namespace_override(self, actor_name, actor_id, actor_suffix, namespace, target_id, target_suffix) -> "bool":
        pass

    def _add_virtual_actor(self, actor_name, actor_id, suffix) -> "bool":
        pass

    def _clear_actor(self, actor_name) -> "bool":
        pass

    def _clear_actor_trackmask_override(self, actor_name):
        pass

    def _enter(self) -> "bool":
        """
        Forces the current state to be 'entry'.  No animations are scheduled.
        """

    def _exit(self, arb, request_id=0) -> "int":
        """
        Executes a tunneling request to the exit state.
        """

    def _get_actor_definition(self, actor_name):
        """
        _get_actor_definition - Returns a tuple containing the information in the actor description for a given actor name.
        """

    def _get_param_sequences(self, actor_id: int, to_state_name: str, from_state_name: str, locked_args: dict = None):
        """
        pairs that represent 
        all valid combinations of parameter values for the given state traversal.
        """

    def _get_params(self, *args):
        """
        Returns a list of dictionaries of the form (parameter name, value pairs that represent 
        all current parameters on the ASM.
        """

    def _get_props_in_traversal(self, from_state, to_state) -> "bool":
        """
        AsmBase_get_props_in_traversal - Returns a dict of actor name/ResourceKeyObject for each prop actor in a give state traversal.
        """

    def _get_resource_key_for_actor(self, actor_name) -> "bool":
        """
        AsmBase_get_resource_key_for_actor - Returns the resource key attached to the actor definition with the given name
        """

    def _get_supported_postures_for_actor(self, actor_name) -> "bool":
        """
        _get_supported_postures_for_actor - Returns a tuple of tuples describing the supported postures, with each configuration specified as (actor_name, name, family, compatibility, carry_left, carry_right, carry_back, surface) for the actor name supplied, or the default if none supplied
        """

    def _remove_virtual_actor(self, actor_name, actor_id, suffix) -> "bool":
        pass

    def _request(self, to_state, arb, request_id=0, interrupt=False) -> "int":
        """
        Requests a given state name
        """

    def _schedule_exit_content(self, arb):
        """
        Schedules the exit content for the last request (if there is any into the provided ARB
        """

    def _set_actor(self, actor_name, actor_id, suffix) -> "bool":
        pass

    def _set_actor_parameter(self, actor_name, actor_id, parameter_name, value) -> "bool":
        pass

    def _set_actor_trackmask_override(self, actor_name, track, trackmask_name):
        pass

    def _set_current_state(self, state_name) -> "bool":
        """
        Forces the current state to be the specified state.  No animations are scheduled.
        """

    def _set_parameter(self, parameter_name, value) -> "bool":
        pass

    def _set_reaction_actor(self, actor):
        pass

    def _set_single_actor_parameter_if_possible(self, actor_name, parameter_name, value) -> "bool":
        pass

    def _traverse(self, from_state, to_state, arb, request_id=0, from_boundary_conditions=False) -> "bool":
        """
        Traverses the graph between two states and adds commands to the provided Arb
        """

    @property
    def actor_instances(self):
        """
        Actor instance data, returns a dict of actor data.
        """

    @actor_instances.setter
    def actor_instances(self, value):
        """
        Actor instance data, returns a dict of actor data.
        """

    @property
    def actors(self):
        """
        Tuple of actors for the ASM.
        """

    @actors.setter
    def actors(self, value):
        """
        Tuple of actors for the ASM.
        """

    @property
    def current_state(self):
        """
        current_state - Returns the current state name as a string.
        """

    @current_state.setter
    def current_state(self, value):
        """
        current_state - Returns the current state name as a string.
        """

    @property
    def parameters(self):
        """
        Tuple of parameters for the ASM.
        """

    @parameters.setter
    def parameters(self, value):
        """
        Tuple of parameters for the ASM.
        """

    @property
    def provided_postures(self):
        """
        provided_postures - Returns a tuple of tuples describing the provided postures, with each configuration specified as (None, name, family, compatibility, carry_left, carry_right, carry_back, surface)
        The initial None is to make the configuration consistent with the actor-specific format
        """

    @provided_postures.setter
    def provided_postures(self, value):
        """
        provided_postures - Returns a tuple of tuples describing the provided postures, with each configuration specified as (None, name, family, compatibility, carry_left, carry_right, carry_back, surface)
        The initial None is to make the configuration consistent with the actor-specific format
        """

    @property
    def public_states(self):
        """
        Tuple of public states for the ASM.
        """

    @public_states.setter
    def public_states(self, value):
        """
        Tuple of public states for the ASM.
        """

    @property
    def state_machine_name(self):
        """
        Returns the name of the ASM.
        """

    @state_machine_name.setter
    def state_machine_name(self, value):
        """
        Returns the name of the ASM.
        """

    @property
    def supported_postures(self):
        """
        supported_postures - Returns a tuple of tuples describing the supported postures, with each configuration specified as (None, name, family, compatibility, carry_left, carry_right, carry_back)
        The initial None is to make the configuration consistent with the actor-specific format
        """

    @supported_postures.setter
    def supported_postures(self, value):
        """
        supported_postures - Returns a tuple of tuples describing the supported postures, with each configuration specified as (None, name, family, compatibility, carry_left, carry_right, carry_back)
        The initial None is to make the configuration consistent with the actor-specific format
        """


CENSOREVENT_STATE_FACE = 8
CENSOREVENT_STATE_FULLBODY = 4
CENSOREVENT_STATE_LHAND = 6
CENSOREVENT_STATE_OFF = 0
CENSOREVENT_STATE_PELVIS = 3
CENSOREVENT_STATE_RHAND = 5
CENSOREVENT_STATE_TODDLERPELVIS = 7
CENSOREVENT_STATE_TORSO = 1
CENSOREVENT_STATE_TORSOPELVIS = 2
EVENT_TIME_FROM_END = 1
EVENT_TIME_FROM_START = 0
TRACK_CARRYBACK = 47000
TRACK_CARRYINTERACTION = 50000
TRACK_CARRYLEFT = 40000
TRACK_CARRYLEFTPLUS = 45000
TRACK_CARRYOVERRIDE = 60000
TRACK_CARRYRIGHT = 30000
TRACK_CARRYRIGHTPLUS = 35000
TRACK_HIGH = 20000
TRACK_HIGHPLUS = 25000
TRACK_IDLE = 1000
TRACK_LOCOMOTION_OVERLAY = 17500
TRACK_LOW = 6000
TRACK_LOWPLUS = 8000
TRACK_NORMAL = 10000
TRACK_NORMALPLUS = 15000
TRACK_ULTRA = 70000
TRACK_ULTRAPLUS = 75000
TRACK_WING_IDLE = 6500
TRACK_WING_OVERLAY = 85000
_ASM_ACTORTYPE_INVALID = -1
_ASM_ACTORTYPE_OBJECT = 1
_ASM_ACTORTYPE_PROP = 2
_ASM_ACTORTYPE_SIM = 0
_ASM_REQUESTRESULT_SUCCESS = 2
_ASM_REQUESTRESULT_TARGET_JUMPED_TO_TARGET_STATE = 1
_ASM_REQUESTRESULT_TARGET_STATE_NOT_FOUND = 0


def enable_native_reaction_event_handling(arg0):
    """
    Enables/disables native reaction event handling
    """


def get_initial_offset_for_clip(arg0):
    """
    Returns the initial offset for a given clip as ((x, y, z), (x, y, z, w))
    """


def get_joint_name_for_hash_from_rig(arg0, arg1):
    """
    Returns the name for a given bone in a specified rig.
    """


def get_joint_name_for_index_from_rig(arg0, arg1):
    """
    Returns the name for a given bone in a specified rig.
    """


def get_joint_transform_from_rig(arg0, arg1):
    """
    Returns the bind-pose transform for a given bone in a specified rig as tuple(pos, quat).
    """


def get_mirrored_joint_name_hash(arg0, arg1):
    """
    Returns the corresponding mirrored joint name hash for a given joint.
    """


def update_post_condition_arb(arg0, arg1):
    """
    Updates a post-condition ARB with the contents of a new ARB
    """
