# Annotations Created by TURBODRIVER

"""
The path module encapsulates access to a generated path.
"""

from typing import *

import _geometry
import _math
import _resourceman
import _terrain
import _trace

class Destination():
    """
    Represents a goal for a path.
    """

    cost: 'float'  # The cost for this position (i.e. the distance added when selecting this)
    group: 'int'  # group for this goal
    handle: 'int'  # user defined data for this goal
    tag: 'int'  # user defined data for this goal
    weight: 'float'  # DEFUNCT: remove after weight->cost refactor

    def __init__(self, location: 'Location' = None, cost: 'float' = 0.0, weight: 'float' = 1.0, tag: 'int' = 0):
        """
        Represents a goal for a path.
        """

    @property
    def has_slot_params(self) -> 'bool':
        """
        Return True if this Goal has locked_params the ASM needs
        """

    @has_slot_params.setter
    def has_slot_params(self, value: 'bool'):
        """
        Return True if this Goal has locked_params the ASM needs
        """

    @property
    def location(self) -> 'Location':
        """
        (routing_location) Location associated with this Destination
        """

    @location.setter
    def location(self, value: 'Location'):
        """
        (routing_location) Location associated with this Destination
        """

    @property
    def orientation(self) -> '_math.Quaternion':
        """
        The 3D orientation associated with this Destination
        """

    @orientation.setter
    def orientation(self, value: '_math.Quaternion'):
        """
        The 3D orientation associated with this Destination
        """

    @property
    def position(self) -> '_math.Vector3':
        """
        The 3D point associated with this Destination
        """

    @position.setter
    def position(self, value: '_math.Vector3'):
        """
        The 3D point associated with this Destination
        """

    @property
    def requires_bind(self):
        """
        Return True if this goal requires a posture rebind
        """

    @requires_bind.setter
    def requires_bind(self, value):
        """
        Return True if this goal requires a posture rebind
        """

    @property
    def routing_surface_id(self):
        """
        (SurfaceIdentifierObject) Surface ID associated with this Destination
        """

    @routing_surface_id.setter
    def routing_surface_id(self, value):
        """
        (SurfaceIdentifierObject) Surface ID associated with this Destination
        """

    @property
    def tag_tuple(self):
        """
        The tag
        """

    @tag_tuple.setter
    def tag_tuple(self, value):
        """
        The tag
        """


class Location():
    """
    Represents a unique location on a routing surface
    """

    def __init__(self, position: '_math.Vector3' = None, orientation: '_math.Quaternion' = None, routing_surface: 'SurfaceIdentifier' = None):
        """
        Represents a unique location on a routing surface
        """

    def get_distance(self, location: 'Location') -> 'float':
        """
        Gets the distance between this location and another, using only x,z coordinates + (3*deltaY).  Args: routing.Location, Returns: (float)distance
        """

    @property
    def orientation(self) -> '_math.Quaternion':
        """
        The 3D orientation associated with this Location
        """

    @orientation.setter
    def orientation(self, value: '_math.Quaternion'):
        """
        The 3D orientation associated with this Location
        """

    @property
    def position(self) -> '_math.Vector3':
        """
        The 3D point associated with this Location
        """

    @position.setter
    def position(self, value: '_math.Vector3'):
        """
        The 3D point associated with this Location
        """

    @property
    def routing_surface(self) -> 'SurfaceIdentifier':
        """
        The routing surface for this Location
        """

    @routing_surface.setter
    def routing_surface(self, value: 'SurfaceIdentifier'):
        """
        The routing surface for this Location
        """

    @property
    def transform(self):
        """
        The world transform for this Location
        """

    @transform.setter
    def transform(self, value):
        """
        The world transform for this Location
        """

    @property
    def world_transform(self):
        """
        The world transform for this Location
        """

    @world_transform.setter
    def world_transform(self, value):
        """
        The world transform for this Location
        """


class PathNode():
    """
    PathNode class, contains goal position, goal orientation, expected duration, and a walk style for that node
    """

    def __init__(self):
        """
        PathNode class, contains goal position, goal orientation, expected duration, and a walk style for that node
        """

    @property
    def action(self):
        """
        The routing action of the node
        """

    @action.setter
    def action(self, value):
        """
        The routing action of the node
        """

    @property
    def index(self):
        """
        Returns index of the node
        """

    @index.setter
    def index(self, value):
        """
        Returns index of the node
        """

    @property
    def is_procedural(self) -> 'bool':
        """
        Is the node procedurally generated
        """

    @is_procedural.setter
    def is_procedural(self, value):
        """
        Is the node procedurally generated
        """

    @property
    def orientation(self):
        """
        Returns the orientation of the node
        """

    @orientation.setter
    def orientation(self, value):
        """
        Returns the orientation of the node
        """

    @property
    def portal_id(self):
        """
        Returns portal id associated with node
        """

    @portal_id.setter
    def portal_id(self, value):
        """
        Returns portal id associated with node
        """

    @property
    def portal_object_id(self):
        """
        Returns portal object id associated with node
        """

    @portal_object_id.setter
    def portal_object_id(self, value):
        """
        Returns portal object id associated with node
        """

    @property
    def position(self):
        """
        Returns the total position of the node
        """

    @position.setter
    def position(self, value):
        """
        Returns the total position of the node
        """

    @property
    def routing_surface_id(self):
        """
        Returns the routing_surface id of this node
        """

    @routing_surface_id.setter
    def routing_surface_id(self, value):
        """
        Returns the routing_surface id of this node
        """

    @property
    def surface_object_id(self):
        """
        Returns surface object id associated with node
        """

    @surface_object_id.setter
    def surface_object_id(self, value):
        """
        Returns surface object id associated with node
        """

    @property
    def time(self):
        """
        Returns the total duration of the node
        """

    @time.setter
    def time(self, value):
        """
        Returns the total duration of the node
        """

    @property
    def tracked_terrain_tags(self):
        """
        Return a list of terrain tag/terrain transition flag pairs for detected terrain transitions on the node, None if no transitions are present
        """

    @tracked_terrain_tags.setter
    def tracked_terrain_tags(self, value):
        """
        Return a list of terrain tag/terrain transition flag pairs for detected terrain transitions on the node, None if no transitions are present
        """

    @property
    def tracked_transitions(self):
        """
        Returns the transition tracked by the node, if any is tracked
        """

    @tracked_transitions.setter
    def tracked_transitions(self, value):
        """
        Returns the transition tracked by the node, if any is tracked
        """

    @property
    def walkstyle(self):
        """
        Returns desired walkstyle for routing over the node
        """

    @walkstyle.setter
    def walkstyle(self, value):
        """
        Returns desired walkstyle for routing over the node
        """


class PathNodeList():
    """
    Class containing the path to follow, primarily a list of path nodes, also contains the currently executing node index, the total path time and the remaining path time
    """

    def __init__(self, nodes: 'Sequence[PathNode]' = ()):
        """
        Class containing the path to follow, primarily a list of path nodes, also contains the currently executing node index, the total path time and the remaining path time
        """

    def __contains__(self, key: 'PathNode') -> 'bool':
        """
        Return key in self.
        """

    def __getitem__(self, key: 'int') -> 'PathNode':
        """
        Return self[key].
        """

    def __len__(self) -> 'int':
        """
        Return len(self).
        """

    def add_goal(self, location: 'Location', cost: 'float', tag: 'Tuple[int, int]', group: 'int' = 0):
        """
        Adds a new goal for the path plan
        """

    def add_node(self, location: 'Location', time: 'float', node_type: 'int', walkstyle: 'int', portal_obj_id: 'int' = 0, portal_id: 'int' = 0, index: 'Optional[int]' = None):
        """
        Adds a new node to the path. (location, time, node_type, walkstyle, | portalObjectId, portalId, index)
        """

    def add_start(self, location: 'Location', cost: 'float', tag: 'Tuple[int, int]'):
        """
        Adds a new start position for the path plan
        """

    def add_waypoint(self, location: 'Location', cost: 'float', tag: 'Tuple[int, int]', group: 'int' = 0):
        """
        Adds a new waypoint for the path plan
        """

    def apply_initial_timing(self, start_time: 'float', walkstyle: 'int', age: 'int', gender: 'int', species: 'int', locomotion_speed: 'float', extra_clearance: 'float' = 1.0, flags: 'int' = 0):
        """
        Sets up initial parameters for a route. Expects orientation (x, y, z, w), position (x, y, z), walkstyle, age, gender and initial server time.
        """

    def bounds(self) -> 'Tuple[_math.Vector3, _math.Vector3]':
        """
        Returns a list of polygons that define path bounds.
        """

    def clear_route_data(self):
        """
        Clears route data generated by previous make_path calls (does not clear goals, origin, etc)
        """

    def clip_nodes(self, start_index: 'int', end_index: 'int'):
        """
        truncate(i, j) 
        Removes everything but the ith node to the jth in the list.
        """

    @property
    def context(self):
        """
        the PathPlanContext for the path
        """

    @context.setter
    def context(self, value):
        """
        the PathPlanContext for the path
        """

    def copy(self, path):
        """
        copy(path) 
        Copies another path object
        """

    @property
    def duration(self):
        """
        total duration of the path
        """

    @duration.setter
    def duration(self, value):
        """
        total duration of the path
        """

    def erase_node(self, index: 'int'):
        """
        Removes node at index
        """

    def finalize(self, loop: 'bool' = False):
        """
        Does final processing on a path. Must be called before any functions that adjust timing on the path.
        """

    def get_goal_by_index(self, index: 'int') -> 'Optional[Destination]':
        """
        get goal by index.  Returns NULL if not found.  Note that the returned goal is a copy so changing the info will not propagate to the path.
        """

    def get_goal_by_tag(self, tag: 'int') -> 'Optional[Destination]':
        """
        get goal by tag.  Returns NULL if not found.  Note that the returned goal is a copy so changing the info will not propagate to the path.
        """

    def goal_results(self) -> 'List[Tuple[int, int]]':
        """
        Returns a list of goal results where each list item is a tuple of (tag, final_score, reason).  Returns an empty list on non-debug builds.
        """

    @property
    def id(self):
        """
        id of path
        """

    @id.setter
    def id(self, value):
        """
        id of path
        """

    @property
    def length(self):
        """
        the total length of the path
        """

    @length.setter
    def length(self, value):
        """
        the total length of the path
        """

    def make_path(self) -> 'bool':
        """
        Plan a path.  Requires that origin and goals have been set.
        """

    def needs_replan(self) -> 'bool':
        """
        Returns True if the path (from the current sub-path and beyond) needs to be re-planned due to a change in the navmesh, False otherwise.
        """

    def node_at_time(self, time: 'float') -> 'Tuple[Location, float, int, int]':
        """
        Returns the path node the sim should be traversing at the given time
        """

    def obstacles(self) -> 'List[int]':
        """
        Returns a list of lists of polygons that define path obstacles per subpath.
        """

    def orientation_at_time(self, time: 'float') -> '_math.Quaternion':
        """
        Returns the orientation on the path as (x, y, z, w) at the given time
        """

    @property
    def origin(self):
        """
        the start location for the path
        """

    @origin.setter
    def origin(self, value):
        """
        the start location for the path
        """

    @property
    def plan_failure_object_id(self):
        """
        possible object that caused the path to fail
        """

    @plan_failure_object_id.setter
    def plan_failure_object_id(self, value):
        """
        possible object that caused the path to fail
        """

    @property
    def plan_failure_path_type(self):
        """
        if failure path was return this is the reason given
        """

    @plan_failure_path_type.setter
    def plan_failure_path_type(self, value):
        """
        if failure path was return this is the reason given
        """

    @property
    def plan_in_progress(self) -> 'bool':
        """
        TRUE if the plan is still in progress; false if the contents are usable
        """

    @plan_in_progress.setter
    def plan_in_progress(self, value):
        """
        TRUE if the plan is still in progress; false if the contents are usable
        """

    @property
    def plan_result(self):
        """
        a value from the Routing::ePathResult enum that explains why a path failed or the type of success
        """

    @plan_result.setter
    def plan_result(self, value):
        """
        a value from the Routing::ePathResult enum that explains why a path failed or the type of success
        """

    @property
    def plan_success(self) -> 'bool':
        """
        TRUE if the path leads to the requested location, FALSE otherwise
        """

    @plan_success.setter
    def plan_success(self, value):
        """
        TRUE if the path leads to the requested location, FALSE otherwise
        """

    def position_at_time(self, time: 'float') -> '_math.Vector3':
        """
        Returns the position on the path as (x, y, z) at the given time
        """

    @property
    def record(self):
        """
        the plan record information
        """

    @record.setter
    def record(self, value):
        """
        the plan record information
        """

    @property
    def selected_start_tag(self):
        """
        associated id of the plan start used
        """

    @selected_start_tag.setter
    def selected_start_tag(self, value):
        """
        associated id of the plan start used
        """

    @property
    def selected_start_tag_tuple(self):
        """
        associated id of the plan start used
        """

    @selected_start_tag_tuple.setter
    def selected_start_tag_tuple(self, value):
        """
        associated id of the plan start used
        """

    @property
    def selected_tag(self):
        """
        associated id of the plan goal used
        """

    @selected_tag.setter
    def selected_tag(self, value):
        """
        associated id of the plan goal used
        """

    @property
    def selected_tag_tuple(self):
        """
        associated id of the plan goal used
        """

    @selected_tag_tuple.setter
    def selected_tag_tuple(self, value):
        """
        associated id of the plan goal used
        """

    @property
    def server_start_time(self):
        """
        server time path starts (ms)
        """

    @server_start_time.setter
    def server_start_time(self, value):
        """
        server time path starts (ms)
        """

    def update_timing(self, walkstyle: 'int', age: 'int', gender: 'int', species: 'int', locomotion_speed: 'float', extra_clearance: 'float' = 1.0):
        """
        Generates proper timing information for a path. Expects a walkstyle, age, gender and time elapsed since route start.
        """


class PathPlanContext():
    """
    routing context for an object that is capable of path planning
    """

    def __init__(self):
        """
        routing context for an object that is capable of path planning
        """

    @property
    def add_path_boundary_obstacle(self):
        """
        A flag (default off) that says whether or not to perform formation collision tests with the walkable path edges.
        """

    @add_path_boundary_obstacle.setter
    def add_path_boundary_obstacle(self, value):
        """
        A flag (default off) that says whether or not to perform formation collision tests with the walkable path edges.
        """

    @property
    def agent_extra_clearance_multiplier(self) -> 'float':
        """
        Sims will 'prefer' to stay a distance equal to (agent_radius * mult) away from obstacles, if possible.
        """

    @agent_extra_clearance_multiplier.setter
    def agent_extra_clearance_multiplier(self, value: 'float'):
        """
        Sims will 'prefer' to stay a distance equal to (agent_radius * mult) away from obstacles, if possible.
        """

    @property
    def agent_goal_radius(self):
        """
        The radius of the agent (in meters) used for goal generation.
        """

    @agent_goal_radius.setter
    def agent_goal_radius(self, value):
        """
        The radius of the agent (in meters) used for goal generation.
        """

    @property
    def agent_height_clearance_override(self):
        """
        If enabled (non-negative), specifies the height of the agent (in meters).  If disabled, the agent's footprint is used to determine the height instead.
        """

    @agent_height_clearance_override.setter
    def agent_height_clearance_override(self, value):
        """
        If enabled (non-negative), specifies the height of the agent (in meters).  If disabled, the agent's footprint is used to determine the height instead.
        """

    @property
    def agent_id(self) -> 'int':
        """
        The ID of the agent.
        """

    @agent_id.setter
    def agent_id(self, value: 'int'):
        """
        The ID of the agent.
        """

    @property
    def agent_name(self):
        """
        The name of the agent.
        """

    @agent_name.setter
    def agent_name(self, value):
        """
        The name of the agent.
        """

    @property
    def agent_path_plan_radius(self):
        """
        The radius of the agent (in meters) used for path planning only if its value is larger than 0.0f.
        """

    @agent_path_plan_radius.setter
    def agent_path_plan_radius(self, value):
        """
        The radius of the agent (in meters) used for path planning only if its value is larger than 0.0f.
        """

    @property
    def agent_position_offset(self):
        """
        When constructing the agent shape or circles using the agent radius, the center will be offset along the agent's forward vector by this vector.
        """

    @agent_position_offset.setter
    def agent_position_offset(self, value):
        """
        When constructing the agent shape or circles using the agent radius, the center will be offset along the agent's forward vector by this vector.
        """

    @property
    def agent_radius(self) -> 'float':
        """
        The radius of the agent (in meters) used for path planning if agent_path_plan_radius is 0.0f. If agent_path_plan_radius is larger than 0.0f, use agent_path_plan_radius as the radius of the agent.
        """

    @agent_radius.setter
    def agent_radius(self, value: 'float'):
        """
        The radius of the agent (in meters) used for path planning if agent_path_plan_radius is 0.0f. If agent_path_plan_radius is larger than 0.0f, use agent_path_plan_radius as the radius of the agent.
        """

    def clear_override_portal_cost(self, portal_id: 'int'):
        """
        clear any overridden portal cost for this portal
        """

    def clone(self) -> 'PathPlanContext':
        """
        Creates a new PathPlanContext and does a deep copy of the existing context into it.
        """

    @property
    def connectivity_handles(self):
        """
        The connectivity_handle_list for this agent.
        """

    @connectivity_handles.setter
    def connectivity_handles(self, value):
        """
        The connectivity_handle_list for this agent.
        """

    @property
    def debug_trace(self):
        """
        A flag (default off) determining whether to print debug information in certain areas of path planning, test_connectivity, etc.
        """

    @debug_trace.setter
    def debug_trace(self, value):
        """
        A flag (default off) determining whether to print debug information in certain areas of path planning, test_connectivity, etc.
        """

    @property
    def disable_fake_portals(self):
        """
        A flag (default off) that says whether or not to disable fake portals such as curbs.
        """

    @disable_fake_portals.setter
    def disable_fake_portals(self, value):
        """
        A flag (default off) that says whether or not to disable fake portals such as curbs.
        """

    def extend(self, other: 'PathPlanContext'):
        """
        Creates a new PathPlanContext which contains a union of permission masks, ignored footprints, and locked portals from self and the other context. All other settings are taken from the context extend() is called on. If there are no relevant changes in the context passed to extend(), None is returned.
        """

    @property
    def footprint_key(self):
        """
        The resource key for the footprint of the object.
        """

    @footprint_key.setter
    def footprint_key(self, value):
        """
        The resource key for the footprint of the object.
        """

    def get_discourage_key_mask(self) -> 'int':
        """
        Gets discourage key mask for footprints we can plan through
        """

    def get_footprint_contour_actions(self) -> 'Tuple[Tuple[int, int], ...]':
        """
        Returns a list of the contour actions (FootprintID, ContourIndex, Action)
        """

    def get_height_clearance_key_mask_flags(self, key_mask: 'int') -> 'int':
        """
        Gets height clearance key mask flags for a given height
        """

    def get_height_clearance_portal_keymask(self, key_mask: 'int') -> 'int':
        """
        Gets clearance portal key mask flags given node keymask
        """

    def get_key_mask(self) -> 'int':
        """
        Gets key mask for footprints we can plan through
        """

    def get_max_wading_depth(self, depth_type: 'int') -> 'float':
        """
        Gets maximum wading depth given node keymask
        """

    def get_name_val_list(self) -> 'List[Tuple[str, Any]]':
        """
        Gets the PathPlanContext members as a list of name, value pairs. Resource Key is a tuple of (Longinstance, Type, Group)
        """

    def get_portal_discourage_key_mask(self) -> 'int':
        """
        Gets discourage key mask for portals we can plan through
        """

    def get_portal_exclusion_key_mask(self) -> 'int':
        """
        Gets exclusion key mask for portals we can plan through
        """

    def get_portal_key_mask(self) -> 'int':
        """
        Gets key mask for portals we can plan through
        """

    @property
    def ghost_route(self):
        """
        A flag (default off) determining whether to plan the path in ghost mode.
        """

    @ghost_route.setter
    def ghost_route(self, value):
        """
        A flag (default off) determining whether to plan the path in ghost mode.
        """

    def ignore_footprint_contour(self, footprint_id: 'int', contour_index: 'int'):
        """
        ignore specified footprint/contour for the path plan which this context will be used for.   Note that there is a cost associated with overrides for EACH path plan, so it's best to only use this for temporary situations.
        """

    @property
    def impassable_goals_auto_fail(self):
        """
        A flag (default off) determining whether goal points in impassable faces will be ignored.  By default, if a goal is in an impassable face, the planner will determine the closest valid point and use that instead as a fail-path.  Turning this flag on for large clouds of goal points is much more efficient.
        """

    @impassable_goals_auto_fail.setter
    def impassable_goals_auto_fail(self, value):
        """
        A flag (default off) determining whether goal points in impassable faces will be ignored.  By default, if a goal is in an impassable face, the planner will determine the closest valid point and use that instead as a fail-path.  Turning this flag on for large clouds of goal points is much more efficient.
        """

    def is_footprint_contour_ignored(self, footprint_id: 'int', contour_index: 'int') -> 'bool':
        """
        return whether the footprint/contour will be ignored for the path plan which this context will be used for
        """

    def lock_portal(self, portal_id: 'int', lock: 'bool' = True):
        """
        DEFUNCT: lock portal for the path plan which this context will be used for.
        """

    def make_footprint_contour_obstacle(self, footprint_id: 'int', contour_index: 'int'):
        """
        make the specified footprint/contour an obstacle for the path plan which this context will be used for
        """

    @property
    def max_goal_clipping_score(self):
        pass

    @max_goal_clipping_score.setter
    def max_goal_clipping_score(self, value):
        pass

    @property
    def max_slope_angle(self):
        """
        If set (non-zero), specifies the maximum angle an agent is allowed to route through.
        """

    @max_slope_angle.setter
    def max_slope_angle(self, value):
        """
        If set (non-zero), specifies the maximum angle an agent is allowed to route through.
        """

    @property
    def object_descriptor(self):
        """
        The name of the object.   Available only in Debug/DebugRelease.
        """

    @object_descriptor.setter
    def object_descriptor(self, value):
        """
        The name of the object.   Available only in Debug/DebugRelease.
        """

    @property
    def object_footprint_id(self):
        """
        The Navmesh Footprint ID of the object.
        """

    @object_footprint_id.setter
    def object_footprint_id(self, value):
        """
        The Navmesh Footprint ID of the object.
        """

    @property
    def object_id(self):
        """
        The ID of the object.
        """

    @object_id.setter
    def object_id(self, value):
        """
        The ID of the object.
        """

    @property
    def object_radius(self):
        """
        The radius of the object (in meters).
        """

    @object_radius.setter
    def object_radius(self, value):
        """
        The radius of the object (in meters).
        """

    def override_footprint_contour_cost(self, footprint_id: 'int', contour_index: 'int', cost: 'float'):
        """
        override cost for the specified footprint/contour for the path plan which this context will be used for
        """

    def override_portal_cost(self, portal_id: 'int', cost: 'float'):
        """
        override the cost of the portal for this context
        """

    @property
    def path_goals_id(self):
        """
        The PathGoalsID for this path
        """

    @path_goals_id.setter
    def path_goals_id(self, value):
        """
        The PathGoalsID for this path
        """

    def remove_footprint_contour_override(self, footprint_id: 'int', contour_index: 'int'):
        """
        removes any cost overrides/ignores/temp footprints of the specified footprint/contours.   Returns True if successful, False if the specified footprint/contour does not exist or there was another error.
        """

    @property
    def route_fail_on_fake_portals(self):
        """
        A flag (default off) which indicates to route fail rather than try to traverse through fake portals.
        """

    @route_fail_on_fake_portals.setter
    def route_fail_on_fake_portals(self, value):
        """
        A flag (default off) which indicates to route fail rather than try to traverse through fake portals.
        """

    def set_discourage_key_mask(self, key_mask: 'int'):
        """
        Sets discourage key mask for footprints we can plan through
        """

    def set_footprint_contour_actions(self, actions: 'Sequence[Tuple[int, int]]'):
        """
        sets a list of the contour actions (FootprintID, ContourIndex, Action)
        """

    def set_key_mask(self, key_mask: 'int'):
        """
        Sets key mask for footprints we can plan through
        """

    def set_portal_discourage_key_mask(self, key_mask: 'int'):
        """
        Sets discourage key mask for portals we can plan through
        """

    def set_portal_exclusion_key_mask(self, key_mask: 'int'):
        """
        Sets exclusion key mask for portals we can plan through
        """

    def set_portal_key_mask(self, key_mask: 'int'):
        """
        Sets key mask for portals we can plan through
        """

    def set_radius_default(self):
        """
        Sets Object radius to default value.
        """

    @property
    def track_transition_indoor_outdoor(self):
        """
        A flag (default off) determining whether to track indoor-outdoor transitions in path nodes.
        """

    @track_transition_indoor_outdoor.setter
    def track_transition_indoor_outdoor(self, value):
        """
        A flag (default off) determining whether to track indoor-outdoor transitions in path nodes.
        """

    @property
    def track_transition_terrain(self):
        """
        A flag (default off) determining whether to track terrain type transitions in path nodes.
        """

    @track_transition_terrain.setter
    def track_transition_terrain(self, value):
        """
        A flag (default off) determining whether to track terrain type transitions in path nodes.
        """

    @property
    def tracked_terrain_tags(self):
        """
        A list of terrain tags to track, when terrain transition tracking is enabled.
        """

    @tracked_terrain_tags.setter
    def tracked_terrain_tags(self, value):
        """
        A list of terrain tags to track, when terrain transition tracking is enabled.
        """

    def unlock_portal(self, portal_id: 'int'):
        """
        DEFUNCT: unlock portal for the path plan which this context will be used for.
        """


class RoutingContext():
    """
    basic routing context for an object that is not capable of path planning
    """

    def __init__(self):
        """
        basic routing context for an object that is not capable of path planning
        """

    def clone(self) -> 'RoutingContext':
        """
        Creates a new RoutingContext and does a deep copy of the existing context into it.
        """

    @property
    def connectivity_groups_need_rebuild(self):
        """
        A flag (default off) determining whether connectivity handles need to be rebuilt.
        """

    @connectivity_groups_need_rebuild.setter
    def connectivity_groups_need_rebuild(self, value):
        """
        A flag (default off) determining whether connectivity handles need to be rebuilt.
        """

    @property
    def connectivity_handles(self):
        """
        The connectivity_handle_list for this object.
        """

    @connectivity_handles.setter
    def connectivity_handles(self, value):
        """
        The connectivity_handle_list for this object.
        """

    @property
    def debug_trace(self):
        """
        A flag (default off) determining whether to print debug information in certain areas of path planning, test_connectivity, etc.
        """

    @debug_trace.setter
    def debug_trace(self, value):
        """
        A flag (default off) determining whether to print debug information in certain areas of path planning, test_connectivity, etc.
        """

    @property
    def footprint_key(self):
        """
        The resource key for the footprint of the object.
        """

    @footprint_key.setter
    def footprint_key(self, value):
        """
        The resource key for the footprint of the object.
        """

    @property
    def ignore_own_footprint(self):
        """
        A flag (default off) determining whether to ignore this object's footprint for various routing functions.
        """

    @ignore_own_footprint.setter
    def ignore_own_footprint(self, value):
        """
        A flag (default off) determining whether to ignore this object's footprint for various routing functions.
        """

    @property
    def impassable_goals_auto_fail(self):
        """
        A flag (default off) determining whether goal points in impassable faces will be ignored.  By default, if a goal is in an impassable face, the planner will determine the closest valid point and use that instead as a fail-path.  Turning this flag on for large clouds of goal points is much more efficient.
        """

    @impassable_goals_auto_fail.setter
    def impassable_goals_auto_fail(self, value):
        """
        A flag (default off) determining whether goal points in impassable faces will be ignored.  By default, if a goal is in an impassable face, the planner will determine the closest valid point and use that instead as a fail-path.  Turning this flag on for large clouds of goal points is much more efficient.
        """

    @property
    def object_descriptor(self):
        """
        The name of the object.   Available only in Debug/DebugRelease.
        """

    @object_descriptor.setter
    def object_descriptor(self, value):
        """
        The name of the object.   Available only in Debug/DebugRelease.
        """

    @property
    def object_footprint_id(self):
        """
        The Navmesh Footprint ID of the object.
        """

    @object_footprint_id.setter
    def object_footprint_id(self, value):
        """
        The Navmesh Footprint ID of the object.
        """

    @property
    def object_id(self) -> 'int':
        """
        The ID of the object.
        """

    @object_id.setter
    def object_id(self, value: 'int'):
        """
        The ID of the object.
        """

    @property
    def object_radius(self):
        """
        The radius of the object (in meters).
        """

    @object_radius.setter
    def object_radius(self, value):
        """
        The radius of the object (in meters).
        """

    def set_radius_default(self):
        """
        Sets Object radius to default value.
        """


class SurfaceIdentifier():
    """
    Represents a unique routing surface.
    """

    primary_id: 'int'  # The primary ID of the surface (e.g. lot or object ID)
    routable_surface_height: 'float'  # routable surface height for object
    secondary_id: 'int'  # The secondary ID of the surface (e.g. level or object sub-surface)
    type: 'int'  # The type code of the surface

    def __init__(self, primary_id: 'int' = 0, secondary_id: 'int' = 0, type: 'int' = 0):
        """
        Represents a unique routing surface.
        """

    def set_to_invalid(self):
        """
        Sets the surface ID to invalid.  Args: None, Returns: None
        """

    @property
    def valid(self):
        """
        Returns True if this surface ID is Valid (i.e. > 0 and < 0xFFFFFFFFFFFFFFFF).
        """

    @valid.setter
    def valid(self, value):
        """
        Returns True if this surface ID is Valid (i.e. > 0 and < 0xFFFFFFFFFFFFFFFF).
        """


class connectivity_handle():
    """
    Represents a handle into the connectivity graph, via a point
    """

    def __init__(self, polygon: 'Optional[_geometry.Polygon]' = None, routing_surface: 'Optional[SurfaceIdentifier]' = None):
        """
        Represents a handle into the connectivity graph, via a point
        """

    @property
    def connectivity_groups(self) -> 'int':
        """
        (uint32_t) Connectivity Groups associated with this connectivity_handle.  Note that if the value is None, the handle is not valid.
        """

    @connectivity_groups.setter
    def connectivity_groups(self, value):
        """
        (uint32_t) Connectivity Groups associated with this connectivity_handle.  Note that if the value is None, the handle is not valid.
        """

    @property
    def connectivity_groups_lite(self) -> 'int':
        """
        (uint32_t) Lite Connectivity Groups associated with this connectivity_handle.  Note that if the value is None, the handle is not valid.
        """

    @connectivity_groups_lite.setter
    def connectivity_groups_lite(self, value):
        """
        (uint32_t) Lite Connectivity Groups associated with this connectivity_handle.  Note that if the value is None, the handle is not valid.
        """

    @property
    def is_current(self):
        """
        {bool} whether or not this connectivity_handle's info is current (i.e. if the navmesh has been updated since this handle's info was set.
        """

    @is_current.setter
    def is_current(self, value):
        """
        {bool} whether or not this connectivity_handle's info is current (i.e. if the navmesh has been updated since this handle's info was set.
        """

    @property
    def polygons(self):
        """
        ((Polygon, ...)) The tuple of polygons representing the geometry of this connectivity handle. This generates a new set of polygons each time it is invoked.
        """

    @polygons.setter
    def polygons(self, value):
        """
        ((Polygon, ...)) The tuple of polygons representing the geometry of this connectivity handle. This generates a new set of polygons each time it is invoked.
        """

    @property
    def routing_surface_id(self):
        """
        (routing.SurfaceIdentifier) The routing surface associated with this connectivity_handle
        """

    @routing_surface_id.setter
    def routing_surface_id(self, value):
        """
        (routing.SurfaceIdentifier) The routing surface associated with this connectivity_handle
        """

    def transform(self, transform: '_math.Transform') -> 'connectivity_handle':
        """
        return a new connectivity_handle that contains the geometry of this handle, transformed by the parameter
        """

    def update(self):
        """
        updates connectivity handle and ensures it's data is current.
        """


class connectivity_handle_list():
    """
    Represents a list of connectivity_handles.  C++ also uses these lists of connectivity_handles, so please use this and don't just copy a bunch of connectivity_handle objects into a normal Python list
    """

    def __init__(self, handles: 'Sequence[connectivity_handle]' = ()):
        """
        Represents a list of connectivity_handles.  C++ also uses these lists of connectivity_handles, so please use this and don't just copy a bunch of connectivity_handle objects into a normal Python list
        """

    def __add__(self, value):
        """
        Return self+value.
        """

    def __bool__(self) -> 'bool':
        """
        self != 0
        """

    def __contains__(self, key) -> 'bool':
        """
        Return key in self.
        """

    def __delitem__(self, key):
        """
        Delete self[key].
        """

    def __getitem__(self, key):
        """
        Return self[key].
        """

    def __iadd__(self, value):
        """
        Implement self+=value.
        """

    def __len__(self) -> 'int':
        """
        Return len(self).
        """

    def __setitem__(self, key, value):
        """
        Set self[key] to value.
        """

    def append(self, h: 'connectivity_handle'):
        """
        append(connectivity_handle h) -> None
        Appends the connectivity_handle h at end of the list.  Note that this is more efficient than calling insert as the connectivity_handle_list is internally stored as an array.
        """

    def clear(self):
        """
        clear() -> None
        Clears the list of all connectivity_handles.
        """

    def insert(self, i: 'int', h: 'connectivity_handle'):
        """
        insert(i, connectivity_handle h) -> None
        Inserts the connectivity_handle h at index i.
        """

    def pop(self, i: 'int' = -1) -> 'connectivity_handle':
        """
        pop(i = -1) -> connectivity_handle
        Removes the ith connectivity_handle of the list (and returns it).  Note that using the default param of -1 is more efficient than popping an item in the middle of the list as the connectivity_handle_list is internally stored as an array.
        """

    def remove(self, h: 'connectivity_handle'):
        """
        remove(connectivity_handle h) -> None
        Removes the connectivity_handle h if it exists in the list.
        """


def add_fence(points: 'Sequence[_math.Vector3]') -> 'int':
    """
    Add a fence to the navmesh operation queue, with a provided context value. c_api_navmesh_fence_callback will becalled when the fence has been processed by the planner thread.
    """


def add_footprint(footprint_id: 'int', compound_polygon: '_geometry.CompoundPolygon', routing_surface: 'SurfaceIdentifier', enabled: 'bool' = True):
    """
    Adds an ObjectRoutingFootprint to the nave mesh and invalidates it
    """


def add_portal(portal_id: 'int', portal_type: 'int', location_in: 'Location', location_out: 'Location', cost: 'float' = 0.0, traversal_cost: 'float' = 0.0, key_mask: 'int' = 0, discourage_mask: 'int' = 0, exclusion_mask: 'int' = 0, portal_obj_id: 'int' = 0):
    """
    Add a portal to the nav mesh.  Requires an entry, exit and portal type.  Returns a handle to the portal.
    """


def add_surface(zone_id: 'int', surface_type: 'int', surface_id: 'int', bounds: 'Tuple[_math.Vector3, _math.Vector3]'):
    """
    Add a surface to navmesh
    """


def estimate_distance_between_multiple_points(sources: 'Sequence[Union[Location, Tuple[_math.Vector3, SurfaceIdentifier], connectivity_handle]]', dests: 'Sequence[Union[Location, Tuple[_math.Vector3, SurfaceIdentifier], connectivity_handle]]', routing_context: 'Optional[RoutingContext]' = None, allow_permissive_connections: 'bool' = False) -> 'Optional[float]':
    """
    Return the shortest distance between sources and dests, as estimated by the router.
    """


def estimate_path_batch(src: 'Sequence[connectivity_handle]', dst: 'Sequence[connectivity_handle]', routing_context: 'Optional[RoutingContext]' = None, flush_planner: 'bool' = False, allow_permissive_connections: 'bool' = False, ignore_objects: 'bool' = False) -> 'List[Tuple[connectivity_handle, connectivity_handle, float]]':
    """
    Returns whether the given connectivity handles are connected (route-able) in the nav mesh
    """


def flush_planner(flush_all: 'bool' = False):
    """
    Flushes the planner, causing a navmesh rebuild if necessary
    """


def get_actor_pitch_roll_at_location(location: 'Location', age: 'int', gender: 'int', species: 'int') -> 'float':
    """
    Return the pitch and roll angle in degrees around XY location, using direction to obtain the two points used to the calculation
    """


def get_blocked_ladder_portals(ladder_id: 'int', zone_id: 'int') -> 'Tuple[int, ...]':
    """
    Returns a bitmask which tells if a top ladder portal is blocked by a wall. A nonzero bit means a blocked portal.
    """


def get_default_agent_extra_clearance_multiplier() -> 'float':
    """
    Get the default Agent Extra Clearance Multiplier.  This is a number from 0.0f to n that is multiplied by the agent's radius during a pathplan to get the 'extra clearance' value.  This extra clearance is the distance that the agent will prefer to stay away from obstacles in most cases, but only if there is room around them.  Note that this value can be overridden in the RoutingContext to change it for an individual pathplan.
    """


def get_default_agent_radius() -> 'float':
    """
    Default agent radius used in pathplanning.  In other words, pathplans will not allow paths to go through areas that are less than double this value (i.e. the diameter).  The agent radius can be overridden for individual pathplans by setting the value in the RoutingContext.  If the value is not overridden in the RoutingContext, however, this default value will be used.   Note that this Cannot be set to a value < the minimum agent radius, which is essentially a hard-coded value used internally by the pathplanner.
    """


def get_default_discouragement_cost() -> 'float':
    """
    Default discouragement cost.   This is really the minimum discouragement cost in practice and any footprint set to a cost less than this will be considered a normal cost.  This cost must be greater than the default traversal cost and less than the default obstacle cost.
    """


def get_default_obstacle_cost() -> 'float':
    """
    the minimum cost for obstacles.   Any footprint of this cost or above is considered impassable in the navmesh.   This cost must be greater than the default discouragement cost.
    """


def get_default_traversal_cost() -> 'float':
    """
    default traversal cost for all areas of the navmesh.
    """


def get_floor_to_ceiling_distance_at_location(location: 'Location') -> 'Optional[float]':
    """
    Returns the distance between the floor and ceiling at a given location
    """


def get_footprint_polys(key: '_resourceman.Key') -> 'List[_geometry.Polygon]':
    """
    Get the footprint polygons keyed by name hash and their enabled status
    """


def get_ladder_levels_and_height(ladder_id: 'int', zone_id: 'int') -> 'Tuple[int, int, float]':
    """
    Get the top level, bottom level, and height of the given ladder.
    """


def get_last_fence() -> 'int':
    """
    Return the last fence ID that was cleared by the pathplanner
    """


def get_min_agent_radius() -> 'float':
    """
    Minimum agent radius.  Any context that attempts to set an agent radius less than this for a pathplan will silently change the value to this minimum.
    """


def get_portals_in_connectivity_path(src: 'Union[connectivity_handle, Location]', dst: 'Union[connectivity_handle, Location]', routing_context: 'Optional[RoutingContext]' = None) -> 'Optional[Tuple[int, ...]]':
    """
    Returns a tuple of portal object IDs (may be empty), or none if no path exists
    """


def get_stair_portal_key_mask(stair_id: 'int', zone_id: 'int' = 0) -> 'int':
    """
    Returns the portal key mask for a given stairid
    """


def get_stair_portals(stair_id: 'int', zone_id: 'int') -> 'Tuple[int, ...]':
    """
    Get the stair portals as a list of lanes.  (lanes)->(up, down)->(top, bottom)
    """


def get_walkstyle_hash_from_resource(key: '_resourceman.Key') -> 'int':
    """
    Return 32bit walkstyle name hash from walkstyle resource key
    """


def get_walkstyle_info(walkstyle_hash: 'int', age: 'int', gender: 'int', species: 'int') -> 'Tuple[float, float]':
    """
    Returns cycle info about walkstyle
    """


def get_walkstyle_info_full(walkstyle_hash: 'int', age: 'int', gender: 'int', species: 'int') -> 'Dict[Union[int, str], Dict[str, float]]':
    """
    Returns dict with info about walkstyle. The keys are the hashed name of the builder type (cycle, start, etc) and the values are dicts with the parameter data.
    """


def get_walkstyle_name_from_resource(key: '_resourceman.Key') -> 'str':
    """
    Return walkstyle name from walkstyle resource key
    """


def get_walkstyle_property(walkstyle: 'int', age: 'int', gender: 'int', species: 'int', property_id: 'int') -> 'Optional[float]':
    """
    Returns the value of the specified property for the walkstyle.
    """


def get_world_bounds() -> 'Tuple[_math.Vector3, _math.Vector3]':
    """
    Gets the min and max bounds of the world (returns a tuple of 2 Vector3 objects, representing the min and max bounds).
    """


def get_world_center() -> '_math.Vector3':
    """
    Returns the coordinates of the world center point.
    """


def get_world_size() -> '_math.Vector3':
    """
    Gets the size of the world (returns a Vector3, but y will always be 0)
    """


def has_walkstyle_info(walkstyle_hash: 'int', age: 'int', gender: 'int', species: 'int') -> 'bool':
    """
    Return True if the specified age/gender/species has the specified walkstyle.
    """


def invalidate_footprint(footprint_id: 'int', zone_id: 'int' = 0):
    """
    Invalidates a footprint in the navmesh by id.
    """


def invalidate_navmesh():
    """
    Calls invalidate on the navmesh so that it will be rebuild on the next access.
    """


def is_3d_point_indoors(location: 'Location') -> 'bool':
    """
    Returns true if a given point is indoors
    """


def is_portal_valid(portal_id: 'int', routing_context: 'Optional[RoutingContext]' = None) -> 'bool':
    """
    Is the portal currently valid
    """


def is_position_in_surface_bounds(pos: '_math.Vector3', routing_surface: 'SurfaceIdentifier', margin: 'float' = 0.0) -> 'bool':
    """
    Return True if the specified point is inside the bounds of the specified surface, False otherwise.
    input: routing.SurfaceIdentifier surfaceID, point (which can be a Vector3, Vector2, or 2 floats (x and z)).
    """


def is_position_in_world_bounds(pos: '_math.Vector3', margin: 'float' = 0.0) -> 'bool':
    """
    Return True if the specified point is inside the world bounds, False otherwise.
    input: float x, float z, routing.SurfaceIdentifier surfaceID.
    """


def planner_build_id() -> 'int':
    """
    Returns the current planner build id
    """


def planner_build_record(record_flags: 'int'):
    """
    Returns the build record by build id
    """


def ray_test(start: 'Location', end: 'Location', routing_context: 'Optional[RoutingContext]' = None, flags: 'int' = 0) -> 'bool':
    """
    Returns true if two points have no blocking objects between them
    """


def ray_test_verbose(start: 'Location', end: 'Location', routing_context: 'Optional[RoutingContext]' = None, flags: 'int' = 0) -> 'int':
    """
    Returns a value indicating the type of blocking footprint intersected by a raytest between two points
    """


def remove_footprint(footprint_id: 'int'):
    """
    Removes an ObjectRoutingFootprint from the nav mesh and invalidates it
    """


def remove_portal(portal_id: 'int'):
    """
    Remove a portal from the navmesh.  Requires an handle to the portal, as returned by add_portal.
    """


def remove_surface(zone_id: 'int', surface_type: 'int', surface_id: 'int'):
    """
    Remove a surface from the navmesh
    """


def set_default_agent_extra_clearance_multiplier(multiplier: 'float'):
    """
    Get the default Agent Extra Clearance Multiplier.  This is a number from 0.0f to n that is multiplied by the agent's radius during a pathplan to get the 'extra clearance' value.  This extra clearance is the distance that the agent will prefer to stay away from obstacles in most cases, but only if there is room around them.  Note that this value can be overridden in the RoutingContext to change it for an individual pathplan.
    """


def set_default_agent_radius(radius: 'float'):
    """
    Default agent radius used in pathplanning.  In other words, pathplans will not allow paths to go through areas that are less than double this value (i.e. the diameter).  The agent radius can be overridden for individual pathplans by setting the value in the RoutingContext.  If the value is not overridden in the RoutingContext, however, this default value will be used.   Note that this Cannot be set to a value < the minimum agent radius, which is essentially a hard-coded value used internally by the pathplanner.
    """


def set_default_discouragement_cost(cost: 'float'):
    """
    Default discouragement cost.   This is really the minimum discouragement cost in practice and any footprint set to a cost less than this will be considered a normal cost.  This cost must be greater than the default traversal cost and less than the default obstacle cost.
    """


def set_default_obstacle_cost(cost: 'float'):
    """
    the minimum cost for obstacles.   Any footprint of this cost or above is considered impassable in the navmesh.   This cost must be greater than the default discouragement cost.
    """


def test_connectivity_batch(src: 'Sequence[Location]', dst: 'Sequence[Destination]', routing_context: 'Optional[RoutingContext]' = None, compute_cost: 'bool' = False, flush_planner: 'bool' = False, allow_permissive_connections: 'bool' = False, ignore_objects: 'bool' = False) -> 'List[Tuple[bool, float]]':
    """
    Returns whether the given connectivity handles are connected (route-able) in the nav mesh
    """


def test_connectivity_permissions_for_handle(handle: 'connectivity_handle', routing_context: 'Optional[RoutingContext]' = None, flush_planner: 'bool' = False) -> 'bool':
    """
    Return True if the provided routing context grants permission to reach the connectivity group of the connectivity_handle
    """


def test_connectivity_pt_pt(loc1: 'Location', loc2: 'Location', routing_context: 'Optional[RoutingContext]' = None, ignore_objects: 'bool' = False) -> 'bool':
    """
    Returns whether the given points are connected (route-able) in the nav mesh
    """


def test_point_placement_in_navmesh(pos: '_math.Vector3', routing_surface: 'SurfaceIdentifier') -> 'bool':
    """
    Performs a test of the specified navmesh surface and point.  Returns True if the point is in a routable area and False if it is not.
    """


def test_polygon_placement_in_navmesh(polygon: '_geometry.Polygon', routing_surface: 'SurfaceIdentifier') -> 'bool':
    """
    Performs a test of the specified navmesh surface and polygon.  Returns True if the polygon does not overlap any unrouteable areas.
    """


def update_portal_cost(portal_id: 'int', cost: 'float'):
    """
    Update the cost of the portal in the navmesh, negative numbers will use the default distance calc
    """


def update_portal_usage_penalty(portal_id: 'int', penalty: 'float'):
    """
    Update the usage penalty of the portal in the navmesh, negative numbers will use the default for the portal type
    """


ESTIMATE_PATH_OPTION_ALWAYS_RETURN_MINIMUM_DISTANCE = 8
ESTIMATE_PATH_OPTION_IGNORE_CONNECTIVITY_HANDLES = 2
ESTIMATE_PATH_OPTION_NO_NEAREST_VALID_POINT_SEARCH = 32
ESTIMATE_PATH_OPTION_RETURN_DISTANCE_FROM_FIRST_CONNECTION_FOUND = 4
ESTIMATE_PATH_OPTION_RETURN_DISTANCE_ON_FAIL = 1
ESTIMATE_PATH_OPTION_ZERO_DISTANCE_IS_OPTIMAL = 16
ESTIMATE_PATH_RESULT_ALL_GOAL_HANDLES_BLOCKED = 512
ESTIMATE_PATH_RESULT_ALL_START_HANDLES_BLOCKED = 32
ESTIMATE_PATH_RESULT_GOAL_LOCATION_BLOCKED = 256
ESTIMATE_PATH_RESULT_GOAL_LOCATION_INVALID = 128
ESTIMATE_PATH_RESULT_GOAL_SURFACE_INVALID = 64
ESTIMATE_PATH_RESULT_NO_CONNECTIVITY = 1024
ESTIMATE_PATH_RESULT_PATHPLANNER_NOT_INITIALIZED = 2
ESTIMATE_PATH_RESULT_START_LOCATION_BLOCKED = 16
ESTIMATE_PATH_RESULT_START_LOCATION_INVALID = 8
ESTIMATE_PATH_RESULT_START_SURFACE_INVALID = 4
ESTIMATE_PATH_RESULT_SUCCESS = 1
ESTIMATE_PATH_RESULT_UNKNOWN_ERROR = 2048
FAIL_PATH_TYPE_BUILD_BLOCKING = 2
FAIL_PATH_TYPE_OBJECT_BLOCKING = 1
FAIL_PATH_TYPE_UNKNOWN = 0
FAIL_PATH_TYPE_UNKNOWN_BLOCKING = 3
FOOTPRINT_DISCOURAGE_KEY_DEFAULT = 0
FOOTPRINT_DISCOURAGE_KEY_LANDINGSTRIP = 1
FOOTPRINT_KEY_DEFAULT = 3
FOOTPRINT_KEY_OFF_LOT = 2
FOOTPRINT_KEY_ON_LOT = 1
FOOTPRINT_KEY_REQUIRE_FLOATING = 32
FOOTPRINT_KEY_REQUIRE_LARGE_HEIGHT = 64
FOOTPRINT_KEY_REQUIRE_LOW_HEIGHT = 1024
FOOTPRINT_KEY_REQUIRE_MEDIUM_HEIGHT = 2048
FOOTPRINT_KEY_REQUIRE_NO_CARRY = 4
FOOTPRINT_KEY_REQUIRE_SMALL_HEIGHT = 8
FOOTPRINT_KEY_REQUIRE_TINY_HEIGHT = 16
FOOTPRINT_KEY_REQUIRE_WADING_DEEP = 4096
FOOTPRINT_KEY_REQUIRE_WADING_MEDIUM = 8192
FOOTPRINT_KEY_REQUIRE_WADING_SHALLOW = 16384
FOOTPRINT_KEY_REQUIRE_WADING_VERY_SHALLOW = 32768
FOOTPRINT_TYPE_BUILD = 4
FOOTPRINT_TYPE_LANDING_STRIP = 2
FOOTPRINT_TYPE_LOT = 3
FOOTPRINT_TYPE_OBJECT = 6
FOOTPRINT_TYPE_OVERRIDE = 7
FOOTPRINT_TYPE_PATH = 5
FOOTPRINT_TYPE_WORLD = 1
GOAL_STATUS_BLOCKED = 256
GOAL_STATUS_COMPONENT_DIFFERENT = 16
GOAL_STATUS_CONNECTIVITY_GROUP_UNREACHABLE = 8
GOAL_STATUS_DUPLICATE_GOAL = 4
GOAL_STATUS_IMPASSABLE = 128
GOAL_STATUS_INVALID_POINT = 2
GOAL_STATUS_INVALID_SURFACE = 1
GOAL_STATUS_LOWER_SCORE = 64
GOAL_STATUS_NOTEVALUATED = 32
GOAL_STATUS_PENDING = 0
GOAL_STATUS_REJECTED_UNKNOWN = 512
GOAL_STATUS_SUCCESS = 1024
GOAL_STATUS_SUCCESS_LOCAL = 1024
GOAL_STATUS_SUCCESS_TRIVIAL = 1024
PATH_RESULT_FAIL_INVALID_START_POINT = 6
PATH_RESULT_FAIL_INVALID_START_SURFACE = 5
PATH_RESULT_FAIL_NO_GOALS = 4
PATH_RESULT_FAIL_NO_PATH = 10
PATH_RESULT_FAIL_PARTIAL_PATH = 9
PATH_RESULT_FAIL_START_POINT_IN_IMPASSABLE_REGION = 7
PATH_RESULT_FAIL_TOO_MANY_CYCLES = 8
PATH_RESULT_SUCCESS_GLOBAL = 3
PATH_RESULT_SUCCESS_LOCAL = 2
PATH_RESULT_SUCCESS_TRIVIAL = 1
PATH_RESULT_UNKNOWN = 0
RAYCAST_HIT_TYPE_IMPASSABLE = 1
RAYCAST_HIT_TYPE_LOS_IMPASSABLE = 2
RAYCAST_HIT_TYPE_NONE = 0
SPECIES_FLAG_RESERVE_INDEX = 0
SURFACETYPE_OBJECT = 2
SURFACETYPE_POOL = 3
SURFACETYPE_UNKNOWN = 0
SURFACETYPE_WORLD = 1
