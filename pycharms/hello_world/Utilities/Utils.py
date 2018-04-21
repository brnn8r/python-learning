"""This module contains useful utilities"""


def is_main(name: str):
    """
    This is a helper method to replace the __name__ == "__main__" check

    :param name: The name of the module to test.
    :return: boolean, true is the current module is the main module, false otherwise.
    """

    return name == "__main__"

def recursive_reverse_string(s: str):
    def tail_helper(inner_s: str, accumulated: str):
        if len(inner_s) <= 0:
            return accumulated
        return tail_helper(inner_s[:-1], accumulated + inner_s[-1:])

    return tail_helper(s, "")


def reverse_string(s: str):
    return s[::-1]