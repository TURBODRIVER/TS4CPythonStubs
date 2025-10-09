"""
Tracing and Logging Interface
"""

LEVEL_DEBUG = 25
LEVEL_ERROR = 150
LEVEL_FATAL = 200
LEVEL_INFO = 50
LEVEL_UNDEFINED = 0
LEVEL_WARN = 100
RESULT_BREAK = 1
RESULT_DISABLE = 2
RESULT_NONE = 0
TYPE_ASSERT = 0
TYPE_FAIL = 3
TYPE_LOG = 4
TYPE_TRACE = 2
TYPE_VERIFY = 1


def config(path, reporter):
    """
    config(path, reporter)
    
    Configure the logging system using the given configuration file.
    
    If a specific reporter is named, only that reporter will be configured.
    """


def log_exception(trace_type, message, group, level, zoneId, frame) -> "result":
    """
    trace_log_exception(trace_type, message, group, level, zoneId, frame) -> result
    
    Log an exception to a file.  The group and level arguments can be used to route
    the message based on its originating system and intended severity.
    
    If a frame object isn't specified, the current stack frame is used.
    """


def prod_trace(type, message, group, level, frame) -> "result":
    """
    prod_trace(type, message, group, level, frame) -> result
    
    Trace a message to the production trace service.  The group and level
    arguments can be used to route the message based on its originating system
    and intended severity.
    
    If a frame object isn't specified, the current stack frame is used.
    """


def reset():
    """
    reset()
    
    Reset the trace system. This clears all existing tracing state.
    """


def set_color(color):
    """
    set_color(color) -> None
    
    Set the console color.
    """


def set_level(level, reporter=None, group=None):
    """
    set_level(level, reporter=None, group=None)
    
    Set the output level for the specified reporter and group combination.
    If reporter is None, all reporters are updated.  If group is None, all
    groups are updated.
    """


def should_trace(trace_type, group, level) -> "result":
    """
    should_trace(trace_type, group, level) -> result
    
    Return whether the given group and level will log according to the
    current configuration of the logging system.
    """


def show_sim_error(message, exc_callstack, simId, objIdList) -> "result":
    """
    show_sim_error(message, exc_callstack, simId, objIdList) -> result
    
    Provides a dialog which displays a simulator exception.
    """


def trace(trace_type, message, group, level, zoneId, frame) -> "result":
    """
    trace(trace_type, message, group, level, zoneId, frame) -> result
    
    Trace a message.  The group and level arguments can be used to route
    the message based on its originating system and intended severity.
    
    If a frame object isn't specified, the current stack frame is used.
    """
