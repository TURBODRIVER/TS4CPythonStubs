# Annotations Created by TURBODRIVER

"""
The module encapsulates behavior related to persistence.
"""

from typing import *

import protocolbuffers.FileSerialization_pb2

def run_persistence_operation(persistence_op_type: 'int', protocol_buffer: 'Union[bytes, protocolbuffers.FileSerialization_pb2.SaveGameData]', save_slot_id: 'int', callback: 'Optional[Callable[[int, bool], None]]') -> 'bool':
    """
    Run python persist option
    """
