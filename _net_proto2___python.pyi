"""
python-proto2 is a module that can be used to enhance proto2 Python API
performance.

It provides access to the protocol buffers C++ reflection API that
implements the basic protocol buffer functions.
"""


def BuildFile():
    """
    Registers a new protocol buffer file in the global C++ descriptor pool.
    """


CPPTYPE_MESSAGE = 10
LABEL_OPTIONAL = 1
LABEL_REPEATED = 3
LABEL_REQUIRED = 2


def NewCDescriptorPool():
    """
    Creates a new C++ descriptor pool.
    """


def NewCMessage():
    """
    Creates a new C++ protocol message, given its full name.
    """


TYPE_MESSAGE = 11
