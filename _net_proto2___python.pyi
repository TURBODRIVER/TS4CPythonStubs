# Annotations Created by TURBODRIVER

"""
python-proto2 is a module that can be used to enhance proto2 Python API
performance.

It provides access to the protocol buffers C++ reflection API that
implements the basic protocol buffer functions.
"""

def BuildFile(serialized_file_descriptor: 'bytes'):
    """
    Registers a new protocol buffer file in the global C++ descriptor pool.
    """


def NewCDescriptorPool():
    """
    Creates a new C++ descriptor pool.
    """


def NewCMessage(full_name: 'str'):
    """
    Creates a new C++ protocol message, given its full name.
    """


CPPTYPE_MESSAGE: 'int' = 10
LABEL_OPTIONAL: 'int' = 1
LABEL_REPEATED: 'int' = 3
LABEL_REQUIRED: 'int' = 2
TYPE_MESSAGE: 'int' = 11
