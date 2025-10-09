"""
Command System
"""


def automation_output(s):
    """
    automation_output(s)
    
    Output the given string to the automation system's output stream.
    """


def client_cheat(s):
    """
    client_cheat(s)
    
    Sends the single string argument (can have spaces) to the client to be executed as a client side cheat.
    """


def describe(filter) -> "tuple":
    """
    describe(filter) -> tuple
    
    Return a tuple containing descriptions of registered commands.  If a
    filter string is given, only commands whose names match the filter will
    be included in the result.
    """


def execute(s) -> "result":
    """
    execute(s) -> result
    
    Execute the given command string.
    """


def output(s):
    """
    output(s)
    
    Output the given string to the command system's output stream.
    """


def register(name, description, usage, callable) -> "bool":
    """
    register(name, description, usage, callable) -> bool
    
    Register callable for the named command.
    """


def unregister(name):
    """
    unregister(name)
    
    Unregister an existing command by name.
    """
