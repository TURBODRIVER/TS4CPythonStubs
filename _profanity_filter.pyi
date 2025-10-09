"""
_profanity_filter module

function for testing strings in the profanity filter
"""


def check(text_to_check) -> "Tuple[int, str]":
    """
    Check an input string for sequences that violate the profanity filter's rules. Sequences that fail are replaced
    with the sequence currently set by _profanity_filter set_substitution_char or default value ('*').
    
    Return value is a tuple, (<number of replacements>, <string with replacements>)
    Annotations Contributors: TURBODRIVER
    """


def scan(text_to_check) -> "int":
    """
    Check an input string for sequences that violate the profanity filter's rules.  Returns the number of sequences that are in violation
    Annotations Contributors: TURBODRIVER
    """
