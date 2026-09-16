# Annotations Created by TURBODRIVER

"""
Telemetry Interface
"""

from typing import *

def log_event(session_id: 'int', module_key: 'str', group_key: 'str', hook_key: 'str', attributes: 'List[Tuple[str, str]]'):
    """
    log_event(session_id, module_key, group_key, hook_key, attributes)
    
    Log telemetry data.
    session_id: The session associated with this event.  Zero means no session.
    """
