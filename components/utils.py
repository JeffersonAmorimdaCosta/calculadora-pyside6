"""
This module contains important functions for the code.
"""

import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')
NUMERIC_EXPRESSION_REGEX = re.compile(r'^[0-9.+*/-]*$')
CONTAIN_DIVISION_BY_ZERO_REGEX = re.compile(r'/\s*0+(\.0+)?\b')


def is_num_or_dot(string: str) -> bool:
    """
    This function checks whether the string contain a number or a dot.
    """

    return bool(NUM_OR_DOT_REGEX.search(string))


def is_valid_number(number: str) -> bool:
    """
    This function checks whether the string is a valid number.
    """

    valid = False
    try:
        float(number)
        valid = True
    except ValueError:
        ...
    return valid


def is_numeric_expression_or_void(expression: str) -> bool:
    """
    This function checks whether the string is a valid numeric expression.
    """

    is_expression = False
    if re.match(NUMERIC_EXPRESSION_REGEX, expression):
        is_expression = True
    return is_expression
