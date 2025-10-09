"""
The placement module encapsulates functions for validating object placement.
"""

from typing import *


class FGLResult():
    """
    A FindGoodLocation Result object.
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
        pass

    @property
    def location(self):
        """
        (routing_location) Location associated with this FGLResult
        """

    @location.setter
    def location(self, value):
        """
        (routing_location) Location associated with this FGLResult
        """

    @property
    def orientation(self):
        """
        (Quaternion) The 3D orientation associated with this FGLResult
        """

    @orientation.setter
    def orientation(self, value):
        """
        (Quaternion) The 3D orientation associated with this FGLResult
        """

    @property
    def position(self):
        """
        (Position) The 3D point associated with this FGLResult
        """

    @position.setter
    def position(self, value):
        """
        (Position) The 3D point associated with this FGLResult
        """

    @property
    def routing_surface_id(self):
        """
        (Location) The 3D point associated with this FGLResult
        """

    @routing_surface_id.setter
    def routing_surface_id(self, value):
        """
        (Location) The 3D point associated with this FGLResult
        """

    @property
    def score(self):
        """
        (float) The score associated with this FGLResult
        """

    @score.setter
    def score(self, value):
        """
        (float) The score associated with this FGLResult
        """

    @property
    def search_type(self):
        """
        (uint32_t) The search_type associated with this FGLResult
        """

    @search_type.setter
    def search_type(self, value):
        """
        (uint32_t) The search_type associated with this FGLResult
        """

    def set_user_data(self, arg0, arg1):
        """
        Sets the UserData stored with this result.
        ARGS: Object, placement.ITEM_TYPE enum value
        Return: None
        """

    @property
    def user_data(self):
        """
        (Object) The user_data associated with this FGLResult
        """

    @user_data.setter
    def user_data(self, value):
        """
        (Object) The user_data associated with this FGLResult
        """

    @property
    def user_data_item_type(self):
        """
        (int32_t) The item_type of the user_data associated with this FGLResult
        """

    @user_data_item_type.setter
    def user_data_item_type(self, value):
        """
        (int32_t) The item_type of the user_data associated with this FGLResult
        """


class FGLResultStrategyDefault():
    """
    Default FindGoodLocation Result Strategy.
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
        pass

    def add_result(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
        """
        Add a result to the search.
        (Args/Keywords:
          location=routing.Location,
          score=float,
          [optional]search_type=placement.FGL_SEARCH_TYPE enum value (defaults to UNKNOWN),
          [optional]user_data=Object,
          [optional]user_data_item_type=placement.ITEM_TYPE enum value (required if user_data is supplied),
        (Returns: True if the result was successfully added, False otherwise
        """

    @property
    def calculate_result_terrain_heights(self):
        """
        (bool [default=false]) Flag if the search will calculate terrain heights for all result points at the end of the search (technically, when finalize_search() is called).  Normally, the results have their y (height) values set to 0.0.  If this flag is turned on, the actual terrain height at that point will be calculated.
        """

    @calculate_result_terrain_heights.setter
    def calculate_result_terrain_heights(self, value):
        """
        (bool [default=false]) Flag if the search will calculate terrain heights for all result points at the end of the search (technically, when finalize_search() is called).  Normally, the results have their y (height) values set to 0.0.  If this flag is turned on, the actual terrain height at that point will be calculated.
        """

    def clear(self):
        """
        Clears results and result params.  Args: None, Returns: None
        """

    @property
    def done_on_max_results(self):
        """
        (bool [default=false]) Flag if search will stop as soon as max_results is reached.   Normally, results will continue through all steps and if max_results is reached, search will continue, replacing the lowest-scored results with anything higher.  If this flag is set, the search will stop as soon as max_results is reached, regardless of result scores.
        """

    @done_on_max_results.setter
    def done_on_max_results(self, value):
        """
        (bool [default=false]) Flag if search will stop as soon as max_results is reached.   Normally, results will continue through all steps and if max_results is reached, search will continue, replacing the lowest-scored results with anything higher.  If this flag is set, the search will stop as soon as max_results is reached, regardless of result scores.
        """

    def get_results(self, *args):
        """
        Results from search.
        (Args: None)
        (Returns: list of tuples (location (type=routing.Location), score (type=float), search_type (type=int enum)))
        """

    @property
    def keep_context_info(self):
        """
        (bool [default=false]) Flag if search will keep context info after search (step) is completed.  Normally, when a search is completed, the context info and intermediate data are cleared.  This means that if a search is called again, it will start from scratch, re-searching previously evaluated data in the search space.  If this option is set, then at the end of the search, the context data will not be cleared and calls to FGLSeaarch::RunSearchStep() will continue where they left off (until the search is done...at which point, the context info will be cleared anyway). Beware, though, setting this option can result in more memory usage than you may expect as some of the intermediate data can get large.
        """

    @keep_context_info.setter
    def keep_context_info(self, value):
        """
        (bool [default=false]) Flag if search will keep context info after search (step) is completed.  Normally, when a search is completed, the context info and intermediate data are cleared.  This means that if a search is called again, it will start from scratch, re-searching previously evaluated data in the search space.  If this option is set, then at the end of the search, the context data will not be cleared and calls to FGLSeaarch::RunSearchStep() will continue where they left off (until the search is done...at which point, the context info will be cleared anyway). Beware, though, setting this option can result in more memory usage than you may expect as some of the intermediate data can get large.
        """

    @property
    def max_results(self):
        """
        (uint32_t [default=0]) Max Number of results that the search will return.  0 means that there is no maximum.
        """

    @max_results.setter
    def max_results(self, value):
        """
        (uint32_t [default=0]) Max Number of results that the search will return.  0 means that there is no maximum.
        """

    @property
    def max_score_threshold(self):
        """
        (float [default=MAX_FLOAT]) Maximum result score for it to be accepted.
        """

    @max_score_threshold.setter
    def max_score_threshold(self, value):
        """
        (float [default=MAX_FLOAT]) Maximum result score for it to be accepted.
        """

    @property
    def min_score_threshold(self):
        """
        (float [default=-MAX_FLOAT]) Minimum result score for it to be accepted.
        """

    @min_score_threshold.setter
    def min_score_threshold(self, value):
        """
        (float [default=-MAX_FLOAT]) Minimum result score for it to be accepted.
        """

    @property
    def num_results(self):
        """
        (uint32_t) Number of results.
        """

    @num_results.setter
    def num_results(self, value):
        """
        (uint32_t) Number of results.
        """

    @property
    def num_results_added(self):
        """
        (uint32_t) Total number of results added (including results that were later cycled out due to higher scores).
        """

    @num_results_added.setter
    def num_results_added(self, value):
        """
        (uint32_t) Total number of results added (including results that were later cycled out due to higher scores).
        """

    def reset(self):
        """
        Clears results.  Args: None, Returns: None
        """


class FGLSearch():
    """
    A FindGoodLocation Search object.
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None):
        pass

    def add_data_to_search_strategies(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
        """
        Add data to all search strategies that match the search_type filter and accept data of the specified type.
        (Args:
          data=object,
          data_type=int(enum value from placement.FGL_SEARCH_DATA_TYPE),
          [optional]search_type=int(mask of OR'd enum values from placement.FGL_SEARCH_TYPE, default=NONE, which will place in all that accept the data_type)
        (Returns: True if the data was added to at least one search strategy, False otherwise
        """

    def add_search_strategy(self, arg0):
        """
        Add a Search Strategy.
        (Args: instance of FGLSearchStrategy (subtype) object)
        (Returns: None)
        """

    def clear(self):
        """
        Clears all data for the search, result_strategy, and all search_strategies, as well as all context info.
        (Args: None)
        (Returns: None)
        """

    def finalize_search(self):
        """
        Finalizes SearchStep values and cleans up context data.  You only need to call this when using search_step().
        If using search(), this is done automatically.
        (Args: None)
        (Returns: True if the search succeeded, False otherwise)
        """

    def get_results(self, *args):
        """
        Gets the results of the Search.
        (Args: None)
        (Returns: list of FGLResult objects)
        """

    def get_search_strategy(self, arg0):
        """
        Get a search strategy.
        (Args: nIndex(uint32_t))
        (Returns: FGLSearchStrategy object or None if the index is invalid)
        """

    @property
    def id(self):
        """
        (uint64_t) ID of this search.
        """

    @id.setter
    def id(self, value):
        """
        (uint64_t) ID of this search.
        """

    @property
    def num_results(self):
        """
        (uint32_t) Number of results returned (so far) for this search.
        """

    @num_results.setter
    def num_results(self, value):
        """
        (uint32_t) Number of results returned (so far) for this search.
        """

    @property
    def num_search_strategies(self):
        """
        (uint32_t) Number of Search Strategies for this search.
        """

    @num_search_strategies.setter
    def num_search_strategies(self, value):
        """
        (uint32_t) Number of Search Strategies for this search.
        """

    def remove_search_strategy(self, arg0):
        """
        Remove a Search Strategy.
        (Args: instance of FGLSearchStrategy (subtype) OR nIndex (uint32_t))(Returns: True if the strategy was removed, False otherwise)
        """

    def reset(self):
        """
        Clears dynamic search data (restrictions, scoring functions, polygons, results, etc.)
        If result_strategy.keep_context_info is True, then the current context info is reset (set back to search step 1),
        otherwise all contexts are deleted.
        (Args: None)
        (Returns: None)
        """

    @property
    def result_strategy(self):
        """
        FGLResultStrategy
        """

    @result_strategy.setter
    def result_strategy(self, value):
        """
        FGLResultStrategy
        """

    def search(self, *args):
        """
        Runs the Search.
        (Args: None)
        (Returns: True if the search succeeded, False otherwise)
        """

    @property
    def search_result(self):
        """
        (enum value (uint32_t)) Search Result.
        """

    @search_result.setter
    def search_result(self, value):
        """
        (enum value (uint32_t)) Search Result.
        """

    def search_step(self, *args):
        """
        Runs a Search Step.
        (Args: None)
        (Returns: True if there are more SearchSteps, False Otherwise)
        """

    @property
    def should_abort_search(self):
        """
        (bool) If this is True, search will not run.
        """

    @should_abort_search.setter
    def should_abort_search(self, value):
        """
        (bool) If this is True, search will not run.
        """

    def validate_input(self, *args):
        """
        Validates that the search has valid input (search strategies, result strategy, etc).
        (Args: None)
        (Returns: True if input is valid, False otherwise)
        """


class FGLSearchStrategyRouting():
    """
    FGL Search Strategy to search the routing navmesh (i.e. PathPlanner space)
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None, kwarg5: Any = None, kwarg6: Any = None, kwarg7: Any = None, kwarg8: Any = None, kwarg9: Any = None, kwarg10: Any = None, kwarg11: Any = None, kwarg12: Any = None, kwarg13: Any = None, kwarg14: Any = None, kwarg15: Any = None, kwarg16: Any = None, kwarg17: Any = None, kwarg18: Any = None, kwarg19: Any = None):
        pass

    def add_ignored_object_id(self, arg0):
        """
        Adds the ObjectID to the Search Strategy's Ignored Object ID list.
        (Args: Object ID
        (Returns: True if the Object ID was successfully added, False otherwise)
        """

    def add_offset_restriction(self, subtype):
        """
        Adds the Offset Restriction to the Search Strategy.
        (Args: Offset Restriction (subtype)
        (Returns: True if the Offset Restriction was successfully added, False otherwise)
        """

    def add_polygon(self, arg0, arg1):
        """
        Adds a Polygon to the Search Strategy.
        (Args: Polygon (subtype), routing.SurfaceIdentifier
        (Returns: True if the Polygon (and surface) was successfully added, False otherwise)
        """

    def add_polygon_constraint(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        Adds the Polygon Constraint to the Search Strategy.
        (Args: Polygon Constraint Object OR Polygon, SurfaceIdentifier
        (Returns: True if the Polygon Constraint was successfully added, False otherwise)
        """

    def add_restriction(self, subtype):
        """
        Adds the Restriction to the Search Strategy.
        (Args: Restriction (subtype)
        (Returns: True if the Restriction was successfully added, False otherwise)
        """

    def add_scoring_function(self, subtype):
        """
        Adds the Scoring Function to the Search Strategy.
        (Args: ScoringFunction (subtype)
        (Returns: True if the ScoringFunction was successfully added, False otherwise)
        """

    @property
    def allow_goals_in_sim_intended_positions(self):
        """
        (bool) Normally goals points are not allowed if they are within the area that another Sim
        intends to occupy.   This flag disables that check.
        """

    @allow_goals_in_sim_intended_positions.setter
    def allow_goals_in_sim_intended_positions(self, value):
        """
        (bool) Normally goals points are not allowed if they are within the area that another Sim
        intends to occupy.   This flag disables that check.
        """

    @property
    def allow_goals_in_sim_positions(self):
        """
        (bool) Normally goals points are not allowed if they are within the area occupied by a Sim
        (excluding the Sim's own position).   This flag disables that check.
        """

    @allow_goals_in_sim_positions.setter
    def allow_goals_in_sim_positions(self, value):
        """
        (bool) Normally goals points are not allowed if they are within the area occupied by a Sim
        (excluding the Sim's own position).   This flag disables that check.
        """

    @property
    def allow_too_close_to_obstacle(self):
        """
        (bool) Normally goals points are not allowed if they are within the Sim's radius of an obstacle.
        Turning this flag disables this check.
        """

    @allow_too_close_to_obstacle.setter
    def allow_too_close_to_obstacle(self, value):
        """
        (bool) Normally goals points are not allowed if they are within the Sim's radius of an obstacle.
        Turning this flag disables this check.
        """

    @property
    def avoid_sim_radius(self):
        """
        (float) When checking against other Sims, those within (sim_radius + avoid_sim_radius) will
        count as collisions (and thus reject the result).  Default = 0.0.
        """

    @avoid_sim_radius.setter
    def avoid_sim_radius(self, value):
        """
        (float) When checking against other Sims, those within (sim_radius + avoid_sim_radius) will
        count as collisions (and thus reject the result).  Default = 0.0.
        """

    def clear(self):
        """
        Clears the strategy options to default values, clears polygons, restrictions, flags, etc.
        (Args: None
        (Returns: None)
        """

    def clear_ignored_object_ids(self):
        """
        Clears the Search Strategy's Ignored Object ID list.
        (Args: None
        (Returns: None)
        """

    def clear_offset_restrictions(self):
        """
        Clears the Offset Restrictions of the Search Strategy.
        (Args: None
        (Returns: None)
        """

    def clear_polygon_constraints(self):
        """
        Clears the Polygon Constraints of the Search Strategy.
        (Args: None
        (Returns: None)
        """

    def clear_polygons(self):
        """
        Clears the Polygons (and associated SurfaceIdentifiers) of the Search Strategy.
        (Args: None
        (Returns: None)
        """

    def clear_restrictions(self):
        """
        Clears the Restrictions of the Search Strategy.
        (Args: None
        (Returns: None)
        """

    def clear_scoring_functions(self):
        """
        Clears the Scoring Functions of the Search Strategy.
        (Args: None
        (Returns: None)
        """

    def clear_scoring_restrictions_and_polygons(self):
        """
        Clears the Scoring Functions, Restrictions, Polygons, and SurfaceIdentifiers of the Search Strategy.
        (Args: None
        (Returns: None)
        """

    @property
    def connectivity_group_position(self):
        """
        If set, the FGL will use the connectivity group of the Vector3 position specified instead of the connectivity group of the start position.
        """

    @connectivity_group_position.setter
    def connectivity_group_position(self, value):
        """
        If set, the FGL will use the connectivity group of the Vector3 position specified instead of the connectivity group of the start position.
        """

    @property
    def contains_anywhere_constraint(self):
        """
        (bool) Flag to determine whether an 'Anywhere' constraint was added to the parameters.
        """

    @contains_anywhere_constraint.setter
    def contains_anywhere_constraint(self, value):
        """
        (bool) Flag to determine whether an 'Anywhere' constraint was added to the parameters.
        """

    @property
    def contains_nowhere_constraint(self):
        """
        (bool) Flag to determine whether a 'Nowhere' constraint was added to the parameters.
        """

    @contains_nowhere_constraint.setter
    def contains_nowhere_constraint(self, value):
        """
        (bool) Flag to determine whether a 'Nowhere' constraint was added to the parameters.
        """

    @property
    def enclosed_room_only(self):
        """
        (bool) Flag to determine whether the goal points will be limited to enclosed room.
        """

    @enclosed_room_only.setter
    def enclosed_room_only(self, value):
        """
        (bool) Flag to determine whether the goal points will be limited to enclosed room.
        """

    def get_offset_info(self):
        """
        Getter for Client-Side OffsetInfo.
        (Args: None
        (Returns: OffsetInfo tuple if successfully constructed. None otherwise.)
        """

    def get_offset_restriction(self, arg0):
        """
        Gets the Offset Restriction stored at the specified index or None on error (index out of bounds, etc).
        (Args: nIdx (uint32_t)
        (Returns: Offset Restriction (subtype) if index is valid, None otherwise)
        """

    def get_polygon(self, arg0):
        """
        Gets the Polygon stored at the specified index or None on error (index out of bounds, etc).
        (Args: nIdx (uint32_t)
        (Returns: Polygon (subtype) if index is valid, None otherwise)
        """

    def get_polygon_constraint(self, arg0):
        """
        Gets the Polygon Constraint stored at the specified index or None on error (index out of bounds, etc).
        (Args: nIdx (uint32_t)
        (Returns: Polygon Constraint if index is valid, None otherwise)
        """

    def get_raytest_info(self):
        """
        Getter for Client-Side RaytestInfo.
        (Args: None
        (Returns: RaytestInfo tuple if successfully constructed. None otherwise.)
        """

    def get_restriction(self, arg0):
        """
        Gets the Restriction stored at the specified index or None on error (index out of bounds, etc).
        (Args: nIdx (uint32_t)
        (Returns: Restriction (subtype) if index is valid, None otherwise)
        """

    def get_routing_surface(self, arg0):
        """
        Gets the SurfaceIdentifier for the Polygon stored at the specified index or None on error (index out of bounds, etc).
        (Args: nIdx (uint32_t)
        (Returns: routing.SurfaceIdentifier if index is valid, None otherwise)
        """

    def get_scoring_function(self, arg0):
        """
        Gets the Scoring Function stored at the specified index or None on error (index out of bounds, etc).
        (Args: nIdx (uint32_t)
        (Returns: ScoringFunction (subtype) if index is valid, None otherwise)
        """

    def get_search_flags(self):
        """
        Gets the search flags held on the search strategy.
        (Args: None
        (Returns: Search Flags.
        """

    def get_water_depth_info(self):
        """
        Getter for the Client-side WaterDepthInfo.
        (Args: None
        (Returns: WaterdepthInfo tuple if successfully constructed. None otherwise.
        """

    @property
    def height_tolerance(self):
        """
        (float) Range of how much height difference we allow between polygon points.
        """

    @height_tolerance.setter
    def height_tolerance(self, value):
        """
        (float) Range of how much height difference we allow between polygon points.
        """

    @property
    def lot_terrain_only(self):
        """
        (bool) Flag to determine whether the goal points will be limited to only lot terrain.
        """

    @lot_terrain_only.setter
    def lot_terrain_only(self, value):
        """
        (bool) Flag to determine whether the goal points will be limited to only lot terrain.
        """

    @property
    def max_distance(self):
        """
        (float) Maximum Distance from Start Location to test before giving up.   -1.0 (default)
        means search until there is no more map to search.
        """

    @max_distance.setter
    def max_distance(self, value):
        """
        (float) Maximum Distance from Start Location to test before giving up.   -1.0 (default)
        means search until there is no more map to search.
        """

    @property
    def max_pond_water_depth(self):
        """
        (float) If provided, each vertex of the test polygon along with its centroid will be tested to determine
        whether the pond water at the test location is at most this deep. Values <= 0 indicate placement in
        ponds is invalid)
        """

    @max_pond_water_depth.setter
    def max_pond_water_depth(self, value):
        """
        (float) If provided, each vertex of the test polygon along with its centroid will be tested to determine
        whether the pond water at the test location is at most this deep. Values <= 0 indicate placement in
        ponds is invalid)
        """

    @property
    def max_steps(self):
        """
        Maximum number of steps before search ends.  Default = 1.  For FGLSearchStrategyRoutingGoals,
        it's best to keep this value at 1.
        """

    @max_steps.setter
    def max_steps(self, value):
        """
        Maximum number of steps before search ends.  Default = 1.  For FGLSearchStrategyRoutingGoals,
        it's best to keep this value at 1.
        """

    @property
    def max_water_depth(self):
        """
        (float) If provided, each vertex of the test polygon along with its centroid will be tested to determine
        whether the ocean water at the test location is at most this deep.  Values <= 0 indicate placement in
        ocean is invalid)
        """

    @max_water_depth.setter
    def max_water_depth(self, value):
        """
        (float) If provided, each vertex of the test polygon along with its centroid will be tested to determine
        whether the ocean water at the test location is at most this deep.  Values <= 0 indicate placement in
        ocean is invalid)
        """

    @property
    def min_distance(self):
        """
        (float) Min Distance from Start Location to start testing. 0.0 (default)
        """

    @min_distance.setter
    def min_distance(self, value):
        """
        (float) Min Distance from Start Location to start testing. 0.0 (default)
        """

    @property
    def min_head_room(self):
        """
        (float) specifies the min headroom required
        """

    @min_head_room.setter
    def min_head_room(self, value):
        """
        (float) specifies the min headroom required
        """

    @property
    def min_pond_water_depth(self):
        """
        (float) If provided, each vertex of the test polygon along with its centroid will be tested to determine
        whether the pond water at the test location is at least this deep. Values <= 0 indicate placement on
        land is invalid)
        """

    @min_pond_water_depth.setter
    def min_pond_water_depth(self, value):
        """
        (float) If provided, each vertex of the test polygon along with its centroid will be tested to determine
        whether the pond water at the test location is at least this deep. Values <= 0 indicate placement on
        land is invalid)
        """

    @property
    def min_water_depth(self):
        """
        (float) If provided, each vertex of the test polygon along with its centroid will be tested to determine
        whether the ocean water at the test location is at least this deep.  Values <= 0 indicate placement on
        land is valid
        """

    @min_water_depth.setter
    def min_water_depth(self, value):
        """
        (float) If provided, each vertex of the test polygon along with its centroid will be tested to determine
        whether the ocean water at the test location is at least this deep.  Values <= 0 indicate placement on
        land is valid
        """

    @property
    def num_ignored_object_ids(self):
        """
        The number of Object IDs in the Search Strategy's Ignored Object ID list.
        """

    @num_ignored_object_ids.setter
    def num_ignored_object_ids(self, value):
        """
        The number of Object IDs in the Search Strategy's Ignored Object ID list.
        """

    @property
    def num_offset_restrictions(self):
        """
        The number of Offset Restrictions associated with this Search Strategy.
        """

    @num_offset_restrictions.setter
    def num_offset_restrictions(self, value):
        """
        The number of Offset Restrictions associated with this Search Strategy.
        """

    @property
    def num_polygons(self):
        """
        The number of Polygons (and SurfaceIdentifiers) associated with this Search Strategy.
        """

    @num_polygons.setter
    def num_polygons(self, value):
        """
        The number of Polygons (and SurfaceIdentifiers) associated with this Search Strategy.
        """

    @property
    def num_polygons_constraints(self):
        """
        The number of Polygon Constraints associated with this Search Strategy.
        """

    @num_polygons_constraints.setter
    def num_polygons_constraints(self, value):
        """
        The number of Polygon Constraints associated with this Search Strategy.
        """

    @property
    def num_restrictions(self):
        """
        The number of Restrictions associated with this Search Strategy.
        """

    @num_restrictions.setter
    def num_restrictions(self, value):
        """
        The number of Restrictions associated with this Search Strategy.
        """

    @property
    def num_scoring_functions(self):
        """
        The number of Scoring Functions associated with this Search Strategy.
        """

    @num_scoring_functions.setter
    def num_scoring_functions(self, value):
        """
        The number of Scoring Functions associated with this Search Strategy.
        """

    @property
    def object_def_id(self):
        """
        (uint64_t) Object def ID of the object being tested. This is only used when testing buildbuy placement,
        but object_id or object_def_id is required when doing so.
        """

    @object_def_id.setter
    def object_def_id(self, value):
        """
        (uint64_t) Object def ID of the object being tested. This is only used when testing buildbuy placement,
        but object_id or object_def_id is required when doing so.
        """

    @property
    def object_def_state_index(self):
        """
        (uint32_t) Object def state index of the object being tested. This is only used when testing buildbuy placement,
        but object_id or object_def_id is required when doing so.
        """

    @object_def_state_index.setter
    def object_def_state_index(self, value):
        """
        (uint32_t) Object def state index of the object being tested. This is only used when testing buildbuy placement,
        but object_id or object_def_id is required when doing so.
        """

    @property
    def object_id(self):
        """
        (uint64_t) Object ID of the object being tested.  This is only used when testing buildbuy placement,
        but object_id or object_def_id is required when doing so.
        """

    @object_id.setter
    def object_id(self, value):
        """
        (uint64_t) Object ID of the object being tested.  This is only used when testing buildbuy placement,
        but object_id or object_def_id is required when doing so.
        """

    @property
    def offset_distance(self):
        """
        (float) Offset distance from test position.
        """

    @offset_distance.setter
    def offset_distance(self, value):
        """
        (float) Offset distance from test position.
        """

    @property
    def position_increment(self):
        """
        (float) Position Increment (in meters) between each test point.  Default is 0.3
        """

    @position_increment.setter
    def position_increment(self, value):
        """
        (float) Position Increment (in meters) between each test point.  Default is 0.3
        """

    @property
    def random_range_orientation(self):
        """
        (float) Range to adjust goal point final orientation.
        """

    @random_range_orientation.setter
    def random_range_orientation(self, value):
        """
        (float) Range to adjust goal point final orientation.
        """

    @property
    def random_range_weighting(self):
        """
        (float) Range to adjust goal point final weighting score.
        """

    @random_range_weighting.setter
    def random_range_weighting(self, value):
        """
        (float) Range to adjust goal point final weighting score.
        """

    @property
    def random_seed(self):
        """
        (uint32_t) Random Seed used for this Search Strategy.
        """

    @random_seed.setter
    def random_seed(self, value):
        """
        (uint32_t) Random Seed used for this Search Strategy.
        """

    @property
    def raytest_end_offset(self):
        """
        (float) End height offset
        """

    @raytest_end_offset.setter
    def raytest_end_offset(self, value):
        """
        (float) End height offset
        """

    @property
    def raytest_ignore_flags(self):
        """
        (uint32) test ignore flags
        """

    @raytest_ignore_flags.setter
    def raytest_ignore_flags(self, value):
        """
        (uint32) test ignore flags
        """

    @property
    def raytest_radius(self):
        """
        (float) radius of the ray
        """

    @raytest_radius.setter
    def raytest_radius(self, value):
        """
        (float) radius of the ray
        """

    @property
    def raytest_start_offset(self):
        """
        (float) Start height offset
        """

    @raytest_start_offset.setter
    def raytest_start_offset(self, value):
        """
        (float) Start height offset
        """

    @property
    def raytest_start_point(self):
        """
        The Vector3 position of the start of the ray
        """

    @raytest_start_point.setter
    def raytest_start_point(self, value):
        """
        The Vector3 position of the start of the ray
        """

    def remove_ignored_object_id(self, arg0):
        """
        Removes the Object ID from the Search Strategy's Ignored Object ID list.
        (Args: Object ID
        (Returns: None)
        """

    def remove_offset_restriction(self, subtype):
        """
        Removes the Offset Restriction to the Search Strategy.
        (Args: Offset Restriction (subtype)
        (Returns: True if the Offset Restriction was successfully removed, False otherwise)
        """

    def remove_polygon(self, subtype):
        """
        Removes the Polygon (and associated SurfaceIdentifier) to the Search Strategy.
        (Args: Polygon (subtype)
        (Returns: True if the Polygon was successfully removed, False otherwise)
        """

    def remove_polygon_constraint(self, arg0):
        """
        Removes the Polygon Constraint to the Search Strategy.
        (Args: Polygon Constraint
        (Returns: True if the Polygon Constraint was successfully removed, False otherwise)
        """

    def remove_restriction(self, subtype):
        """
        Removes the Restriction to the Search Strategy.
        (Args: Restriction (subtype)
        (Returns: True if the Restriction was successfully removed, False otherwise)
        """

    def remove_scoring_function(self, subtype):
        """
        Removes the Scoring Function to the Search Strategy.
        (Args: ScoringFunction (subtype)
        (Returns: True if the ScoringFunction was successfully removed, False otherwise)
        """

    def reset(self):
        """
        Clears the Scoring Functions, Restrictions (both normal and offset restrictions), Polygons (and associated SurfaceIdentifiers),
        and search-step related flags of the Search Strategy.
        (Args: None
        (Returns: None)
        """

    @property
    def rotation_increment(self):
        """
        (float) Rotation Increment (in radians) between each test rotation.  Default is PI / 8.
        """

    @rotation_increment.setter
    def rotation_increment(self, value):
        """
        (float) Rotation Increment (in radians) between each test rotation.  Default is PI / 8.
        """

    @property
    def routing_context(self):
        """
        (RoutingContext) RoutingContext of the object or Sim associated with this Search Strategy.
        """

    @routing_context.setter
    def routing_context(self, value):
        """
        (RoutingContext) RoutingContext of the object or Sim associated with this Search Strategy.
        """

    def set_offset_info(self):
        """
        Setter for Client-Side OffsetInfo. Argument must not be None.
        (Args: OffsetInfo
        (Returns: True if successfully set, False otherwise)
        """

    def set_raytest_info(self):
        """
        Setter for Client-Side RaytestInfo. Argument must not be None.
        (Args: RaytestInfo
        (Returns: True if successfully set, False otherwise)
        """

    def set_search_flags(self):
        """
        Sets the search flags held on the search strategy. Argument must not be None.
        (Args: Search Flags (UInt32)
        (Returns: True if search flags set successfully, False otherwise.
        """

    def set_water_depth_info(self):
        """
        Setter for the Client-side WaterDepthInfo. Argument must not be None.
        (Args: WaterdepthInfo
        (Returns: True if successfully set, False otherwise.
        """

    @property
    def should_raytest(self):
        """
        (bool) When this flag is turned on, FGL Searches will raytest between the start and end positions against
        footprints/buildbuy obstacles.
        """

    @should_raytest.setter
    def should_raytest(self, value):
        """
        (bool) When this flag is turned on, FGL Searches will raytest between the start and end positions against
        footprints/buildbuy obstacles.
        """

    @property
    def should_test_buildbuy(self):
        """
        (bool) When this flag is turned on, FGL Searches will test against placement
        footprints/buildbuy obstacles.
        """

    @should_test_buildbuy.setter
    def should_test_buildbuy(self, value):
        """
        (bool) When this flag is turned on, FGL Searches will test against placement
        footprints/buildbuy obstacles.
        """

    @property
    def should_test_routing(self):
        """
        (bool) When this flag is turned on, FGL Searches will test against routing footprints.
        If neither this flag or should_test_buildbuy is set, the search will behave as if this flag
        is turned on.
        """

    @should_test_routing.setter
    def should_test_routing(self, value):
        """
        (bool) When this flag is turned on, FGL Searches will test against routing footprints.
        If neither this flag or should_test_buildbuy is set, the search will behave as if this flag
        is turned on.
        """

    @property
    def spiral_inwards(self):
        """
        (bool) When this flag is turned on, FGL Searches will spiral inwards rather than out
        use in conjunction with min_distance.
        """

    @spiral_inwards.setter
    def spiral_inwards(self, value):
        """
        (bool) When this flag is turned on, FGL Searches will spiral inwards rather than out
        use in conjunction with min_distance.
        """

    @property
    def start_location(self):
        """
        (routing_location) Starting Location associated with this Search Strategy.
        """

    @start_location.setter
    def start_location(self, value):
        """
        (routing_location) Starting Location associated with this Search Strategy.
        """

    @property
    def start_object_contour_index(self):
        """
        (uint32_t) Contour Index of the (navmesh)FootprintID of start object.   Used when
        stay_in_same_connectivity_group or stay_in_connected_connectivity_group are set, and allows the
        algorithm to ignore that footprint when searching for the start connectivity group.  If this is
        not set, it is unlikely that the flags will work.
        """

    @start_object_contour_index.setter
    def start_object_contour_index(self, value):
        """
        (uint32_t) Contour Index of the (navmesh)FootprintID of start object.   Used when
        stay_in_same_connectivity_group or stay_in_connected_connectivity_group are set, and allows the
        algorithm to ignore that footprint when searching for the start connectivity group.  If this is
        not set, it is unlikely that the flags will work.
        """

    @property
    def start_object_footprint_id(self):
        """
        (uint64_t) (navmesh)FootprintID of start object.   Used when stay_in_same_connectivity_group
        or stay_in_connected_connectivity_group are set, and allows the algorithm to ignore that
        footprint when searching for the start connectivity group.  If this is not set, it is unlikely
        that the flags will work.
        """

    @start_object_footprint_id.setter
    def start_object_footprint_id(self, value):
        """
        (uint64_t) (navmesh)FootprintID of start object.   Used when stay_in_same_connectivity_group
        or stay_in_connected_connectivity_group are set, and allows the algorithm to ignore that
        footprint when searching for the start connectivity group.  If this is not set, it is unlikely
        that the flags will work.
        """

    @property
    def start_offset_orientation(self):
        """
        The Quaternion start orientation of the test polygon.  Only used when offset_distance > 0.0.
        In that case, the start_orientation controls the pivot point around which the offset-polygon is
        moved and the start_offset_orientation controls the orientation of the polygon itself.
        """

    @start_offset_orientation.setter
    def start_offset_orientation(self, value):
        """
        The Quaternion start orientation of the test polygon.  Only used when offset_distance > 0.0.
        In that case, the start_orientation controls the pivot point around which the offset-polygon is
        moved and the start_offset_orientation controls the orientation of the polygon itself.
        """

    @property
    def start_orientation(self):
        """
        The Quaternion start orientation associated with this Search Strategy.
        """

    @start_orientation.setter
    def start_orientation(self, value):
        """
        The Quaternion start orientation associated with this Search Strategy.
        """

    @property
    def start_position(self):
        """
        The Vector3 start position associated with this Search Strategy.
        """

    @start_position.setter
    def start_position(self, value):
        """
        The Vector3 start position associated with this Search Strategy.
        """

    @property
    def start_routing_surface(self):
        """
        (SurfaceIdentifierObject) Starting Surface ID associated with this Search Strategy.
        """

    @start_routing_surface.setter
    def start_routing_surface(self, value):
        """
        (SurfaceIdentifierObject) Starting Surface ID associated with this Search Strategy.
        """

    @property
    def stay_in_connected_connectivity_group(self):
        """
        (bool) Flag to determine whether the goal points will be limited to a connectivity group that
        is connected to the start location.
        """

    @stay_in_connected_connectivity_group.setter
    def stay_in_connected_connectivity_group(self, value):
        """
        (bool) Flag to determine whether the goal points will be limited to a connectivity group that
        is connected to the start location.
        """

    @property
    def stay_in_current_block(self):
        """
        (bool) Flag to determine whether the goal points will be limited to the block the search starts in
        """

    @stay_in_current_block.setter
    def stay_in_current_block(self, value):
        """
        (bool) Flag to determine whether the goal points will be limited to the block the search starts in
        """

    @property
    def stay_in_lot(self):
        """
        (bool) Flag to determine whether the goal points will be limited to inside the lot bounds
        """

    @stay_in_lot.setter
    def stay_in_lot(self, value):
        """
        (bool) Flag to determine whether the goal points will be limited to inside the lot bounds
        """

    @property
    def stay_in_same_connectivity_group(self):
        """
        (bool) Flag to determine whether the goal points will be limited to the same connectivity
        group as the start location.
        """

    @stay_in_same_connectivity_group.setter
    def stay_in_same_connectivity_group(self, value):
        """
        (bool) Flag to determine whether the goal points will be limited to the same connectivity
        group as the start location.
        """

    @property
    def stay_outside(self):
        """
        (bool) Flag to determine whether the goal points will be limited to outside
        """

    @stay_outside.setter
    def stay_outside(self, value):
        """
        (bool) Flag to determine whether the goal points will be limited to outside
        """

    @property
    def terrain_tags(self):
        """
        The terrain tags that must be matched for this test.  If any are provided, each vertex of the test
        polygon along with its centroid will be tested for the most dominant terrain tag at that location.
        If the found tag at any test location does not match one of the specified tags, the test will fail.
        """

    @terrain_tags.setter
    def terrain_tags(self, value):
        """
        The terrain tags that must be matched for this test.  If any are provided, each vertex of the test
        polygon along with its centroid will be tested for the most dominant terrain tag at that location.
        If the found tag at any test location does not match one of the specified tags, the test will fail.
        """

    @property
    def use_random_orientation(self):
        """
        (bool) Flag to determine whether goal points will each randomly adjust their final orientation
        within a range specified by random_range_orientation.
        """

    @use_random_orientation.setter
    def use_random_orientation(self, value):
        """
        (bool) Flag to determine whether goal points will each randomly adjust their final orientation
        within a range specified by random_range_orientation.
        """

    @property
    def use_random_weighting(self):
        """
        (bool) Flag to determine whether goal points will each randomly adjust their final weighting
        within a range specified by random_range_weighting.
        """

    @use_random_weighting.setter
    def use_random_weighting(self, value):
        """
        (bool) Flag to determine whether goal points will each randomly adjust their final weighting
        within a range specified by random_range_weighting.
        """

    @property
    def use_sim_footprint(self):
        """
        (bool) Flag to determine whether to use a circle with the Sim's radius as the test polygon.
        If this option is set, any polygons added will be ignored.
        """

    @use_sim_footprint.setter
    def use_sim_footprint(self, value):
        """
        (bool) Flag to determine whether to use a circle with the Sim's radius as the test polygon.
        If this option is set, any polygons added will be ignored.
        """

    def validate_input(self):
        """
        Validates that the search strategy has valid input.
        (Args: None)
        (Returns: True if input is valid, False otherwise)
        """


class FGLSearchStrategyRoutingGoals():
    """
    FGL Search Strategy to find valid routing goal points.
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None, kwarg5: Any = None, kwarg6: Any = None, kwarg7: Any = None, kwarg8: Any = None, kwarg9: Any = None, kwarg10: Any = None):
        pass

    def add_polygon(self, arg0, arg1):
        """
        Adds the Scoring Function to the Search Strategy.
        (Args: Polygon (subtype), routing.SurfaceIdentifier
        (Returns: True if the Polygon (and surface) was successfully added, False otherwise)
        """

    def add_restriction(self, subtype):
        """
        Adds the Restriction to the Search Strategy.
        (Args: Restriction (subtype)
        (Returns: True if the Restriction was successfully added, False otherwise)
        """

    def add_scoring_function(self, subtype):
        """
        Adds the Scoring Function to the Search Strategy.
        (Args: ScoringFunction (subtype)
        (Returns: True if the ScoringFunction was successfully added, False otherwise)
        """

    @property
    def allow_goals_in_sim_intended_positions(self):
        """
        (uint32_t) Normally goals points are not allowed if they are within the area that another
        Sim intends to occupy.   This flag disables that check.
        """

    @allow_goals_in_sim_intended_positions.setter
    def allow_goals_in_sim_intended_positions(self, value):
        """
        (uint32_t) Normally goals points are not allowed if they are within the area that another
        Sim intends to occupy.   This flag disables that check.
        """

    @property
    def allow_goals_in_sim_positions(self):
        """
        (uint32_t) Normally goals points are not allowed if they are within the area occupied by
        a Sim (excluding the Sim's own position).   This flag disables that check.
        """

    @allow_goals_in_sim_positions.setter
    def allow_goals_in_sim_positions(self, value):
        """
        (uint32_t) Normally goals points are not allowed if they are within the area occupied by
        a Sim (excluding the Sim's own position).   This flag disables that check.
        """

    @property
    def allow_too_close_to_obstacle(self):
        """
        (uint32_t) Normally goals points are not allowed if they are within the Sim's radius of
        an obstacle.  Turning this flag disables this check.
        """

    @allow_too_close_to_obstacle.setter
    def allow_too_close_to_obstacle(self, value):
        """
        (uint32_t) Normally goals points are not allowed if they are within the Sim's radius of
        an obstacle.  Turning this flag disables this check.
        """

    def clear(self):
        """
        Clears the strategy options to default values, clears polygons, restrictions, flags, etc.
        (Args: None
        (Returns: None)
        """

    def clear_polygons(self, *args):
        """
        Clears the Polygons (and associated SurfaceIdentifiers) of the Search Strategy.
        (Args: None
        (Returns: None)
        """

    def clear_restrictions(self, *args):
        """
        Clears the Restrictions of the Search Strategy.
        (Args: None
        (Returns: None)
        """

    def clear_scoring_functions(self, *args):
        """
        Clears the Scoring Functions of the Search Strategy.
        (Args: None
        (Returns: None)
        """

    def clear_scoring_restrictions_and_polygons(self, *args):
        """
        Clears the Scoring Functions, Restrictions, Polygons, and SurfaceIdentifiers of the Search Strategy.
        (Args: None
        (Returns: None)
        """

    @property
    def contains_anywhere_constraint(self):
        """
        (uint32_t) Flag to determine whether an 'Anywhere' constraint was added to the parameters.
        """

    @contains_anywhere_constraint.setter
    def contains_anywhere_constraint(self, value):
        """
        (uint32_t) Flag to determine whether an 'Anywhere' constraint was added to the parameters.
        """

    @property
    def contains_nowhere_constraint(self):
        """
        (uint32_t) Flag to determine whether a 'Nowhere' constraint was added to the parameters.
        """

    @contains_nowhere_constraint.setter
    def contains_nowhere_constraint(self, value):
        """
        (uint32_t) Flag to determine whether a 'Nowhere' constraint was added to the parameters.
        """

    def get_polygon(self, arg0):
        """
        Gets the Polygon stored at the specified index or None on error (index out of bounds, etc).
        (Args: nIdx (uint32_t)
        (Returns: Polygon (subtype) if index is valid, None otherwise)
        """

    def get_restriction(self, arg0):
        """
        Gets the Restriction stored at the specified index or None on error (index out of bounds, etc).
        (Args: nIdx (uint32_t)
        (Returns: Restriction (subtype) if index is valid, None otherwise)
        """

    def get_routing_surface(self, arg0):
        """
        Gets the SurfaceIdentifier for the Polygon stored at the specified index or None on error (index out of bounds, etc).
        (Args: nIdx (uint32_t)
        (Returns: routing.SurfaceIdentifier if index is valid, None otherwise)
        """

    def get_scoring_function(self, arg0):
        """
        Gets the Scoring Function stored at the specified index or None on error (index out of bounds, etc).
        (Args: nIdx (uint32_t)
        (Returns: ScoringFunction (subtype) if index is valid, None otherwise)
        """

    def get_search_flags(self):
        """
        Gets the search flags held on the search strategy.
        (Args: None
        (Returns: Search Flags.
        """

    def get_water_depth_info(self):
        """
        Getter for the Client-side WaterDepthInfo.
        (Args: None
        (Returns: WaterdepthInfo tuple if successfully constructed. None otherwise.
        """

    @property
    def goal_density(self):
        """
        (float) Desired number of goals per square meter.
        """

    @goal_density.setter
    def goal_density(self, value):
        """
        (float) Desired number of goals per square meter.
        """

    @property
    def max_fails_per_face(self):
        """
        (int32_t) Max number of times potential goal points can get discarded before face
        itself gets discarded from future consideration.
        """

    @max_fails_per_face.setter
    def max_fails_per_face(self, value):
        """
        (int32_t) Max number of times potential goal points can get discarded before face
        itself gets discarded from future consideration.
        """

    @property
    def max_goals_per_face(self):
        """
        (int32_t) Max number of goal points allowed per face (regardless of goal_density setting).
        """

    @max_goals_per_face.setter
    def max_goals_per_face(self, value):
        """
        (int32_t) Max number of goal points allowed per face (regardless of goal_density setting).
        """

    @property
    def max_steps(self):
        """
        Maximum number of steps before search ends.  Default = 1.  For
        FGLSearchStrategyRoutingGoals, it's best to keep this value at 1.
        """

    @max_steps.setter
    def max_steps(self, value):
        """
        Maximum number of steps before search ends.  Default = 1.  For
        FGLSearchStrategyRoutingGoals, it's best to keep this value at 1.
        """

    @property
    def num_polygons(self):
        """
        The number of Polygons (and SurfaceIdentifiers) associated with this Search Strategy.
        """

    @num_polygons.setter
    def num_polygons(self, value):
        """
        The number of Polygons (and SurfaceIdentifiers) associated with this Search Strategy.
        """

    @property
    def num_restrictions(self):
        """
        The number of Restrictions associated with this Search Strategy.
        """

    @num_restrictions.setter
    def num_restrictions(self, value):
        """
        The number of Restrictions associated with this Search Strategy.
        """

    @property
    def num_scoring_functions(self):
        """
        The number of Scoring Functions associated with this Search Strategy.
        """

    @num_scoring_functions.setter
    def num_scoring_functions(self, value):
        """
        The number of Scoring Functions associated with this Search Strategy.
        """

    @property
    def random_range_orientation(self):
        """
        (float) Range to adjust goal point final orientation.
        """

    @random_range_orientation.setter
    def random_range_orientation(self, value):
        """
        (float) Range to adjust goal point final orientation.
        """

    @property
    def random_range_weighting(self):
        """
        (float) Range to adjust goal point final weighting score.
        """

    @random_range_weighting.setter
    def random_range_weighting(self, value):
        """
        (float) Range to adjust goal point final weighting score.
        """

    @property
    def random_seed(self):
        """
        (uint32_t) Random Seed used for this Search Strategy.
        """

    @random_seed.setter
    def random_seed(self, value):
        """
        (uint32_t) Random Seed used for this Search Strategy.
        """

    def remove_polygon(self, subtype):
        """
        Removes the Polygon (and associated SurfaceIdentifier) to the Search Strategy.
        (Args: Polygon (subtype)
        (Returns: True if the Polygon was successfully removed, False otherwise)
        """

    def remove_restriction(self, subtype):
        """
        Removes the Restriction to the Search Strategy.
        (Args: Restriction (subtype)
        (Returns: True if the Restriction was successfully removed, False otherwise)
        """

    def remove_scoring_function(self, subtype):
        """
        Removes the Scoring Function to the Search Strategy.
        (Args: ScoringFunction (subtype)
        (Returns: True if the ScoringFunction was successfully removed, False otherwise)
        """

    def reset(self):
        """
        Clears the Scoring Functions, Restrictions (both normal and offset restrictions), Polygons (and associated SurfaceIdentifiers),
        and search-step related flags of the Search Strategy.
        (Args: None
        (Returns: None)
        """

    @property
    def routing_context(self):
        """
        (RoutingContext) RoutingContext of the Object or Sim associated with this Search Strategy.
        """

    @routing_context.setter
    def routing_context(self, value):
        """
        (RoutingContext) RoutingContext of the Object or Sim associated with this Search Strategy.
        """

    def set_search_flags(self):
        """
        Gets the search flags held on the search strategy. Arguments must not be None.
        (Args: Search Flags (UInt32)
        (Returns: True if search flags set successfully, False otherwise.
        """

    def set_water_depth_info(self):
        """
        Setter for the Client-side WaterDepthInfo. Arguments must not be None.
        (Args: WaterdepthInfo
        (Returns: True if successfully set, False otherwise.
        """

    @property
    def should_test_buildbuy(self):
        """
        (uint32_t) When this flag is turned on, FGL Searches will test against placement
        footprints/buildbuy obstacles.
        """

    @should_test_buildbuy.setter
    def should_test_buildbuy(self, value):
        """
        (uint32_t) When this flag is turned on, FGL Searches will test against placement
        footprints/buildbuy obstacles.
        """

    @property
    def should_test_routing(self):
        """
        (uint32_t) When this flag is turned on, FGL Searches will test against routing footprints.
        If neither this flag or should_test_buildbuy is set, the search will behave as if this flag
        is turned on.
        """

    @should_test_routing.setter
    def should_test_routing(self, value):
        """
        (uint32_t) When this flag is turned on, FGL Searches will test against routing footprints.
        If neither this flag or should_test_buildbuy is set, the search will behave as if this flag
        is turned on.
        """

    @property
    def start_location(self):
        """
        (routing_location) Starting Location associated with this Search Strategy.
        """

    @start_location.setter
    def start_location(self, value):
        """
        (routing_location) Starting Location associated with this Search Strategy.
        """

    @property
    def start_orientation(self):
        """
        The 3D start orientation associated with this Search Strategy.
        """

    @start_orientation.setter
    def start_orientation(self, value):
        """
        The 3D start orientation associated with this Search Strategy.
        """

    @property
    def start_position(self):
        """
        The 3D start point associated with this Search Strategy.
        """

    @start_position.setter
    def start_position(self, value):
        """
        The 3D start point associated with this Search Strategy.
        """

    @property
    def start_routing_surface(self):
        """
        (SurfaceIdentifierObject) Starting Surface ID associated with this Search Strategy.
        """

    @start_routing_surface.setter
    def start_routing_surface(self, value):
        """
        (SurfaceIdentifierObject) Starting Surface ID associated with this Search Strategy.
        """

    @property
    def stay_in_same_connectivity_group(self):
        """
        (uint32_t) Flag to determine whether the goal points will be limited to the same
        connectivity group as the start location.
        """

    @stay_in_same_connectivity_group.setter
    def stay_in_same_connectivity_group(self, value):
        """
        (uint32_t) Flag to determine whether the goal points will be limited to the same
        connectivity group as the start location.
        """

    @property
    def use_random_orientation(self):
        """
        (uint32_t) Flag to determine whether goal points will each randomly adjust their final
        orientation within a range specified by random_range_orientation.
        """

    @use_random_orientation.setter
    def use_random_orientation(self, value):
        """
        (uint32_t) Flag to determine whether goal points will each randomly adjust their final
        orientation within a range specified by random_range_orientation.
        """

    @property
    def use_random_weighting(self):
        """
        (uint32_t) Flag to determine whether goal points will each randomly adjust their final
        weighting within a range specified by random_range_weighting.
        """

    @use_random_weighting.setter
    def use_random_weighting(self, value):
        """
        (uint32_t) Flag to determine whether goal points will each randomly adjust their final
        weighting within a range specified by random_range_weighting.
        """

    def validate_input(self, *args):
        """
        Validates that the search strategy has valid input.
        (Args: None)
        (Returns: True if input is valid, False otherwise)
        """


FGL_SEARCH_DATA_TYPE_FLAG_CONTAINS_ANYWHERE_CONSTRAINT = 8
FGL_SEARCH_DATA_TYPE_FLAG_CONTAINS_NOWHERE_CONSTRAINT = 7
FGL_SEARCH_DATA_TYPE_POLYGON = 2
FGL_SEARCH_DATA_TYPE_POLYGON_CONSTRAINT = 4
FGL_SEARCH_DATA_TYPE_RESTRICTION = 5
FGL_SEARCH_DATA_TYPE_ROUTING_CONTEXT = 6
FGL_SEARCH_DATA_TYPE_SCORING_FUNCTION = 3
FGL_SEARCH_DATA_TYPE_START_LOCATION = 1
FGL_SEARCH_DATA_TYPE_UNKNOWN = 0
FGL_SEARCH_RESULT_FAIL_BUILDBUY_SYSTEM_UNAVAILABLE = 5
FGL_SEARCH_RESULT_FAIL_CANNOT_LOCK_PATHPLANNER = 4
FGL_SEARCH_RESULT_FAIL_CONTAINS_NOWHERE_CONSTRAINT = 14
FGL_SEARCH_RESULT_FAIL_FAILED_RAYTEST_INTERSECTION = 15
FGL_SEARCH_RESULT_FAIL_INCOMPATIBLE_RESULT_STRATEGY = 12
FGL_SEARCH_RESULT_FAIL_INCOMPATIBLE_SEARCH_STRATEGY = 11
FGL_SEARCH_RESULT_FAIL_INVALID_INPUT = 7
FGL_SEARCH_RESULT_FAIL_INVALID_INPUT_OBJECT_ID = 10
FGL_SEARCH_RESULT_FAIL_INVALID_INPUT_POLYGON = 9
FGL_SEARCH_RESULT_FAIL_INVALID_INPUT_START_LOCATION = 8
FGL_SEARCH_RESULT_FAIL_LOT_UNAVAILABLE = 6
FGL_SEARCH_RESULT_FAIL_NO_GOALS_FOUND = 13
FGL_SEARCH_RESULT_FAIL_PATHPLANNER_NOT_INITIALIZED = 3
FGL_SEARCH_RESULT_FAIL_UNKNOWN = 16
FGL_SEARCH_RESULT_IN_PROGRESS = 2
FGL_SEARCH_RESULT_NOT_INITIALIZED = 1
FGL_SEARCH_RESULT_SUCCESS = 0
FGL_SEARCH_TYPE_NONE = 0
FGL_SEARCH_TYPE_ROUTING = 1
FGL_SEARCH_TYPE_ROUTING_GOALS = 2
GOAL_TYPE_BAD = 1
GOAL_TYPE_FAILURE = 2
GOAL_TYPE_GOOD = 0
ITEMTYPE_GOAL = 7
ITEMTYPE_GOAL_SLOT = 8
ITEMTYPE_ROUTABLE_OBJECT_SURFACE = 32
ITEMTYPE_ROUTE_GOAL_PENALIZER = 31
ITEMTYPE_ROUTE_GOAL_SUPPRESSOR = 30
ITEMTYPE_SIM_INTENDED_POSITION = 6
ITEMTYPE_SIM_POSITION = 5
ITEMTYPE_SIM_ROUTING_CONTEXT = 1
ITEMTYPE_UNKNOWN = 0
NON_SUPPRESSED_FAILURE_GOAL_SCORE = -1.1754943508222875e-38


class ObjectQuadTree():
    """
    ObjectQuadTree(zoneID) -> A QuadTree used for efficient 2.5D (i.e. 2D + surface) spatial queries of objects within a zone
    """

    def __init__(self, arg0):
        pass

    def insert(self, object, objectID, objecItemType, bounds, level, bIgnoreLevel):
        """
        qt.insert(object, objectID, objecItemType, bounds, level, bIgnoreLevel)
        Inserts 'object' (of objectItemType with ID objectID) into the ObjectQuadTree
        with the specified bounds and level, or modifies the itemType, bounds
        and/or level for an existing object
        """

    def query(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None, kwarg5: Any = None):
        """
        qt.query(bounds, level = 0, objectItemType = ITEMTYPE_UNKNOWN, nFlags = OBJECT_QUAD_TREE_QUERY_FLAG_NONE) -> [object, ...]
        A list of tuples (object, objectItemType) which were found within 'bounds' and 'level'.
        If 'objectItemType' is specified, the search will only return objects of that type.
        """

    def remove(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
        """
        qt.remove(objectID, objectItemType)
        Removes object with specified ID and type from the ObjectQuadTree
        """


class ScoringFunctionAngular():
    """
    Represents a helper object to score points using an angular scoring function
    where points are scored by measuring the angle between the vectors formed by
      center -> a point in the direction of the ideal_angle
      center -> scored point
    If that angle is <= ideal_angle_width, the score is 1.0
    If max_angle_width > 0 and ideal_angle_width < angle < (ideal_angle_width + max_angle_width),
      the score is 1 - ((angle - ideal_angle_width)/max_angle_width)
    if the angle > (ideal_angle_width + max_angle_width), the score is 0
    """

    def __init__(self, arg0, arg1, arg2, arg3):
        pass

    @property
    def center(self):
        """
        center point
        """

    @center.setter
    def center(self, value):
        """
        center point
        """

    def get_score(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        Gets score (normalized to [0,1] for a given point and routing_surface.
        While a routing_surface can be passed as an optional second arg, it is ignored for
        this type of scoring function.
        ARGS:
          (Vector3)point,
          (routing.SurfaceIdentifier, ignored)routing_surface
        """

    @property
    def ideal_angle(self):
        """
        ideal angle
        """

    @ideal_angle.setter
    def ideal_angle(self, value):
        """
        ideal angle
        """

    @property
    def ideal_angle_width(self):
        """
        an angular difference < ideal_angle_width is scored 1.0
        """

    @ideal_angle_width.setter
    def ideal_angle_width(self, value):
        """
        an angular difference < ideal_angle_width is scored 1.0
        """

    @property
    def max_angle_width(self):
        """
        an angular difference > (ideal_angle_width + max_angle_width) is scored 0
        """

    @max_angle_width.setter
    def max_angle_width(self, value):
        """
        an angular difference > (ideal_angle_width + max_angle_width) is scored 0
        """

    @property
    def routing_surface(self):
        """
        routing surface (always invalid for this type of Scoring Function)
        """

    @routing_surface.setter
    def routing_surface(self, value):
        """
        routing surface (always invalid for this type of Scoring Function)
        """

    def set_params(self, arg0, arg1, arg2, arg3):
        """
        Sets Params for scoring function.
        ARGS:
          (Vector3)center,
          (float/radians)ideal_angle,
          (float/radians)ideal_angle_width,
          (float/radians)max_angle_width
        """


class ScoringFunctionLinear():
    """
    Represents a helper object to score potential goals using a linear scoring function (i.e. dist from a line)
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
        pass

    def get_score(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        Gets score (normalized to [0,1] for a given point and routing_surface.
        If routing_surface is not passed, or the scoring function has no associated routing_surface,
        then the routing_surface is ignored, otherwise, if the routing_surfaces do not match, the score is 0.
        ARGS:
          (Vector3)point,
          (routing.SurfaceIdentifier, optional:default = routing.SurfaceIdentifier.kInvalidID)routing_surface
        """

    @property
    def ideal_distance(self):
        """
        (float) points that are closer than this distance are scored 1.0
        """

    @ideal_distance.setter
    def ideal_distance(self, value):
        """
        (float) points that are closer than this distance are scored 1.0
        """

    @property
    def max_distance(self):
        """
        (float) points that are farther than this distance are scored 0.0
        """

    @max_distance.setter
    def max_distance(self, value):
        """
        (float) points that are farther than this distance are scored 0.0
        """

    @property
    def point1(self):
        """
        Line Point 1
        """

    @point1.setter
    def point1(self, value):
        """
        Line Point 1
        """

    @property
    def point2(self):
        """
        Line Point 2
        """

    @point2.setter
    def point2(self, value):
        """
        Line Point 2
        """

    @property
    def routing_surface(self):
        """
        routing surface (Default is invalid, which basically ignores surfaces when GetScore is called)
        """

    @routing_surface.setter
    def routing_surface(self, value):
        """
        routing surface (Default is invalid, which basically ignores surfaces when GetScore is called)
        """

    def set_params(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
        """
        Sets Params for scoring function.
        Points are scored by measuring distance from line formed by initial point and angle,
        then normalized to [0,1] where:
        distance < ideal_distance is scored as 1,
        ideal_distance < distance < max_distance is scored as 1->0,
        and distance >= max_distance is scored as 0.
        If routing_surface is not passed, calls to get_score will ignore the routing_surface.
        ARGS:
          (Vector3)point1,
          (Vector3)point2,
          (float)ideal_distance,
          (float)max_distance,
          (routing.SurfaceIdentifier, optional:default = routing.SurfaceIdentifier.kInvalidID)routing_surface
        """


class ScoringFunctionPolygon():
    """
    Represents a helper object to score potential goals using a polygon.  Points inside the polygon are always given a 1.0 score, otherwise they are scored as a linear function of distance from the nearest polygon edge.
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None):
        pass

    def get_score(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        Gets score (normalized to [0,1] for a given point and routing_surface.
        If routing_surface is not passed, or the scoring function has no associated routing_surface,
        then the routing_surface is ignored, otherwise, if the routing_surfaces do not match, the score is 0.
        ARGS:
          (Vector3)point,
          (routing.SurfaceIdentifier, optional:default = routing.SurfaceIdentifier.kInvalidID)routing_surface
        """

    @property
    def ideal_distance(self):
        """
        (float) points that are outside the polygon and are closer than this distance are scored 1.0
        """

    @ideal_distance.setter
    def ideal_distance(self, value):
        """
        (float) points that are outside the polygon and are closer than this distance are scored 1.0
        """

    @property
    def max_distance(self):
        """
        (float) points that are outside the polygon and are farther than this distance are scored 0.0
        """

    @max_distance.setter
    def max_distance(self, value):
        """
        (float) points that are outside the polygon and are farther than this distance are scored 0.0
        """

    @property
    def polygon(self):
        """
        Polygon
        """

    @polygon.setter
    def polygon(self, value):
        """
        Polygon
        """

    @property
    def routing_surface(self):
        """
        routing surface (Default is invalid, which basically ignores surfaces when GetScore is called)
        """

    @routing_surface.setter
    def routing_surface(self, value):
        """
        routing surface (Default is invalid, which basically ignores surfaces when GetScore is called)
        """

    def set_params(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None):
        """
        Sets Params for scoring function.  Points are scored by testing
        if the point is in the polygon (if so, score is 1.0),
        else measuring distance from the point to the nearest edge of the polygon,
        then normalized to [0,1] where:
          distance < ideal_distance is scored as 1,
          ideal_distance < distance < max_distance is scored as 1->0,
          and distance >= max_distance is scored as 0.
        ARGS:
          (Polygon)polygon,
          (float, optional:default = 0.0)ideal_distance,
          (float, optional:default = 0.0)max_distance
          (routing.SurfaceIdentifier, optional:default = routing.SurfaceIdentifier.kInvalidID)routing_surface
        """


class ScoringFunctionRadial():
    """
    Represents a helper object to score potential goals using a radial scoring function (i.e. dist from a radius)
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
        pass

    @property
    def center(self):
        """
        center point
        """

    @center.setter
    def center(self, value):
        """
        center point
        """

    def get_score(self, kwarg0: Any = None, kwarg1: Any = None):
        """
        Gets score (normalized to [0,1] for a given point and routing_surface.
        If routing_surface is not passed, or the scoring function has no associated routing_surface,
        then the routing_surface is ignored, otherwise, if the routing_surfaces do not match, the score is 0.
        ARGS:
          (Vector3)point,
          (routing.SurfaceIdentifier, optional:default = routing.SurfaceIdentifier.kInvalidID)routing_surface
        """

    @property
    def max_distance(self):
        """
        points that are farther than this distance are scored 0.0
        """

    @max_distance.setter
    def max_distance(self, value):
        """
        points that are farther than this distance are scored 0.0
        """

    @property
    def optimal_distance_from_center(self):
        """
        optimal distance from center
        """

    @optimal_distance_from_center.setter
    def optimal_distance_from_center(self, value):
        """
        optimal distance from center
        """

    @property
    def optimal_width(self):
        """
        points that are closer to optimal_distance_from_center than this are score 1.0
        """

    @optimal_width.setter
    def optimal_width(self, value):
        """
        points that are closer to optimal_distance_from_center than this are score 1.0
        """

    @property
    def routing_surface(self):
        """
        routing surface (Default is invalid, which basically ignores surfaces when GetScore is called)
        """

    @routing_surface.setter
    def routing_surface(self, value):
        """
        routing surface (Default is invalid, which basically ignores surfaces when GetScore is called)
        """

    def set_params(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
        """
        Sets Params for scoring function.
        Points are scored by measuring distance from line formed by initial point and angle,
        then normalized to [0,1] where:
          distance < ideal_distance is scored as 1,
          ideal_distance < distance < max_distance is scored as 1->0,
          and distance >= max_distance is scored as 0.
        ARGS:
          (Vector3)point1,
          (Vector3)point2,
          (float)ideal_distance,
          (float)max_distance
          (routing.SurfaceIdentifier, optional:default = routing.SurfaceIdentifier.kInvalidID)routing_surface
        """


def add_placement_footprint(arg0, arg1, arg2, arg3, arg4, arg5):
    pass


def generate_routing_goals_for_polygon(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None, kwarg5: Any = None, kwarg6: Any = None, kwarg7: Any = None, kwarg8: Any = None, kwarg9: Any = None, kwarg10: Any = None, kwarg11: Any = None, kwarg12: Any = None, kwarg13: Any = None, kwarg14: Any = None, kwarg15: Any = None, kwarg16: Any = None, kwarg17: Any = None, kwarg18: Any = None, kwarg19: Any = None, kwarg20: Any = None, kwarg21: Any = None, kwarg22: Any = None, kwarg23: Any = None, kwarg24: Any = None):
    """
    TODO: Write docstring
    """


def get_accurate_placement_footprint_polygon(arg0, arg1, arg2, arg3):
    """
    Return the first valid/enabled placement footprint polygon in the footprint resource
    """


def get_object_height():
    """
    Return the height of the object from its footprint.
    """


def get_object_surface_footprint_polygon(arg0, arg1, arg2, arg3):
    """
    Return the first valid/enabled object surface footprint polygon in the footprint resource
    """


def get_placement_footprint_bounds(kwarg0: Any = None, kwarg1: Any = None):
    """
    Return the untransformed bounds of the Compound Polygon for the footprint.
    """


def get_placement_footprint_compound_polygon(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
    """
    Return all valid polygons in the footprint resource as a CompoundPolygon
    """


def get_placement_footprint_polygon(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
    """
    Gets the polygon for the object's footprint.
      Args: (Vector3)Position, (Quaternion)Orientation, (routing_surface)routing_surface, (resource key)placement_footprint_id
      Return: Polygon or None if the params are invalid.
    """


def get_routing_footprint_polygon(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None):
    """
    Return the largest valid/enabled routing footprint polygon in the footprint resource
    """


def get_sim_quadtree_for_zone(arg0):
    pass


def has_object_surface_footprint(arg0):
    """
    Return if the object there is an object surface polygon in the footprint resource
    """


def ray_intersects_placement_3d(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None, kwarg4: Any = None, kwarg5: Any = None, kwarg6: Any = None):
    pass


def remove_placement_footprint():
    pass


def surface_supports_object_placement(arg0, arg1):
    """
    Test whether a surface can support the placement of a given object definition
    """


def test_footprint_intersection(arg0, arg1, arg2, arg3, arg4):
    """
    Test whether a collection of circles intersects with a specified footprint.
    """


def test_object_placement(arg0, arg1, arg2, arg3):
    """
    Returns whether or not the object with the given resource key can be placed at the given position and orientation
    """


def validate_los_source_location(arg0):
    """
    Test whether a location is a reasonable place to generate an LOS constraint around
    """


def validate_sim_location(kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None, kwarg3: Any = None):
    """
    Test whether a location is a reasonable place to stand according to a routing context and a radius.
    """
