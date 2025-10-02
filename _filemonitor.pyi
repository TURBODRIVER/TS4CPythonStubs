"""
File Monitoring System

The following change filter flags are available:

  FILTER_FILENAME      - File name changes
  FILTER_DIRNAME       - Directory name changes
  FILTER_ATTRIBS       - File attribute changes
  FILTER_SIZE          - File size changes
  FILTER_WRITES        - "Last Write" time changes
  FILTER_READS         - "Last Access" time changes
  FILTER_CREATION      - Creation file time changes
  FILTER_SECURITY      - Security-descriptor changes

The following actions are available:
  ACTION_ADDED         - The file was added to the directory
  ACTION_REMOVED       - The file was removed from the directory
  ACTION_MODIFIED      - The file was modified (time, attribs, etc.)
  ACTION_RENAMED_OLD   - The file was renamed (old name)
  ACTION_RENAMED_NEW   - The file was renamed (new name)
"""

from typing import *

ACTION_ADDED = 1
ACTION_MODIFIED = 3
ACTION_REMOVED = 2
ACTION_RENAMED_NEW = 5
ACTION_RENAMED_OLD = 4


class DirectoryMonitor():
    """
    DirectoryMonitor(path, filter=CT_MTIME, subdirs=True)
    
    A directory monitor is capable of watching a directory (or directory
    hierarchy) for file system changes.  The user periodically polls for
    a list of changed files.
    """

    def __init__(self, kwarg0: Any = None, kwarg1: Any = None, kwarg2: Any = None):
        pass

    @property
    def path(self):
        """
        The monitored directory
        """

    @path.setter
    def path(self, value):
        """
        The monitored directory
        """

    def poll(self) -> "list":
        """
        -> list
        
        Poll the watched directory for a list of file changes.  If no changes
        have been detected, None is returned.  Otherwise, the result will be a
        list of (filename, action tuples.
        """


FILTER_ATTRIBS = 4
FILTER_CREATION = 64
FILTER_DIRNAME = 2
FILTER_FILENAME = 1
FILTER_READS = 32
FILTER_SECURITY = 256
FILTER_SIZE = 8
FILTER_WRITES = 16
