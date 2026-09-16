# Annotations Created by TURBODRIVER

"""
Command System
"""

from typing import *

def automation_output(s: 'str', session_id: 'int' = 0):
    """
    automation_output(s)
    
    Output the given string to the automation system's output stream.
    """


def client_cheat(s: 'str', session_id: 'int' = 0):
    """
    client_cheat(s)
    
    Sends the single string argument (can have spaces) to the client to be executed as a client side cheat.
    """


def describe(filter: 'str' = "") -> 'Tuple[Tuple[str, str, str], ...]':
    """
    describe(filter) -> tuple
    
    Return a tuple containing descriptions of registered commands.  If a
    filter string is given, only commands whose names match the filter will
    be included in the result.
    """


def execute(s: 'str', session_id: 'int' = 0) -> 'bool':
    """
    execute(s) -> result
    
    Execute the given command string.
    """


def output(s: 'str', session_id: 'int' = 0):
    """
    output(s)
    
    Output the given string to the command system's output stream.
    """


def register(name: 'str', description: 'str', usage: 'str', callback: 'Callable[..., None]') -> 'bool':
    """
    register(name, description, usage, callable) -> bool
    
    Register callable for the named command.
    """


def unregister(name: 'str') -> 'bool':
    """
    unregister(name)
    
    Unregister an existing command by name.
    """
