"""Replace each char with alphabet position,
ignore case and non alphabet chars"""

import string


def alphabet_position(text):
    """Replace with alphabet position"""

    return " ".join([str(string.ascii_lowercase.index(x) + 1)
                     for x in "".join([x.lower()
                                       for x in text
                                       if x.lower()
                                       in string.ascii_lowercase])])


def best_practice(text):
    """return with alphabet position"""

    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
