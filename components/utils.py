import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def is_num_or_dot(string: str):
    """
    This function checks whether the string contain a number or a dot.
    """

    return bool(NUM_OR_DOT_REGEX.search(string))
