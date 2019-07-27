"""A pangram sentence which all letter (ant case)
are allmost one time present in full alphabet list"""

import string


def is_pangram(sentence):
    """Return if sentence is a pangram"""

    return all((x in sentence.lower())
               for x in string.ascii_lowercase[:26])
