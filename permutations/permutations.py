"""Return unique permutations"""

from itertools import permutations


def permut(string):
    """Unique permutations"""

    return set("".join(x) for x in list(permutations(string)))


"""Best practice"""


def permut_best(string):
    """Best practice"""

    return list("".join(p) for p in set(permutations(string)))
