"""
Telemetry Interface
"""


def log_event(session_id, module_key, group_key, hook_key, attributes):
    """
    Log telemetry data.
    session_id: The session associated with this event.  Zero means no session.
    """
