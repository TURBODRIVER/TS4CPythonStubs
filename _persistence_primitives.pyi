# Annotations Created by TURBODRIVER

"""
The primitive module encapsulates behavior related     to operations that take time to complete.
"""

from typing import *

def factory(primitive_type: 'int', callback: 'Callable[..., None]', user_data: 'Optional[Any]', context: 'Optional[Any]'):
    """
    Bind a native Python Persist primitive
    """


DATA = 1
DONE = 0
PersistVersion = 5
