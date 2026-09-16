# Annotations Created by TURBODRIVER

"""
_profanity_filter module

function for testing strings in the profanity filter
"""

from typing import *

def check(text_to_check: 'str') -> 'Tuple[int, str]':
    """
    Check an input string for sequences that violate the profanity filter's rules. Sequences that fail are replaced
    with the sequence currently set by _profanity_filter set_substitution_char or default value ('*').
    
    Return value is a tuple, (<number of replacements>, <string with replacements>)
    """


def scan(text_to_check: 'str') -> 'int':
    """
    Check an input string for sequences that violate the profanity filter's rules.  Returns the number of sequences that are in violation
    """
